/**
 * Reveal.js RevealPointerSync Plugin
 */
window.RevealPointerSync = (function() {
  
  let windowType = window.location.search.includes('receiver') ? 'NOTES' : 'MAIN';
  let speakerWindow = null;
  let currentSlideWindow = null;
  let pointer = null;
  let isPointerActive = false;
  
  // Base pointer size (ratio of the slide width)
  const POINTER_SIZE_RATIO = 1 / 100;  // 1% of the slide width (halved from upstream's 2%)

  // Create the laser pointer shape with an initial size
  function createPointer() {
    const p = document.createElement('div');
    p.id = 'reveal-pointer-sync';
    
    p.style.cssText = `
      position: fixed;
      border-radius: 50%;
      background: rgba(255, 0, 0, 0.7);
      border: 2px solid rgba(255, 255, 255, 0.9);
      pointer-events: none;
      z-index: 9999;
      display: none;
      transform: translate(-50%, -50%);
      transition: width 0.05s, height 0.05s, border-width 0.05s;
    `;
    document.body.appendChild(p);
    
    return p;
  }
  
  // Transform slide coordinates into relative coordinates
  function getSlideCoordinates(clientX, clientY) {
    const slides = document.querySelector('.reveal .slides');
    if (!slides) return null;
    
    const rect = slides.getBoundingClientRect();
    const relX = (clientX - rect.left) / rect.width;
    const relY = (clientY - rect.top) / rect.height;
    
    return { relX, relY };
  }
  
  // Convert relative coordinates to actual coordinates and size
  function getActualCoordinates(relX, relY) {
    const slides = document.querySelector('.reveal .slides');
    if (!slides) return null;
    
    const rect = slides.getBoundingClientRect();
    
    // Calculate the pointer size from the slide width
    const pointerSize = rect.width * POINTER_SIZE_RATIO;
    
    return {
      x: rect.left + rect.width * relX,
      y: rect.top + rect.height * relY,
      size: pointerSize
    };
  }
  
  // Show the pointer (dynamically adjust the size)
  function showPointer(x, y, size) {
    if (pointer) {
      const borderWidth = Math.max(size * 0.1, 1);  // 10% of the size (minimum: 1 px)
      
      pointer.style.left = x + 'px';
      pointer.style.top = y + 'px';
      pointer.style.width = size + 'px';
      pointer.style.height = size + 'px';
      pointer.style.borderWidth = borderWidth + 'px';
      pointer.style.display = 'block';
    }
  }
  
  // Hide the pointer
  function hidePointer() {
    if (pointer) {
      pointer.style.display = 'none';
    }
  }

  // Only show the pointer while actually presenting, not while just
  // browsing/editing the deck in a normal windowed tab. "Presenting" is
  // read from the Fullscreen API rather than any keybinding, since every
  // key-based signal we tried (Alt+P, Shift+P, F8) risked being intercepted
  // by something on the presenter's machine before the page ever saw it.
  // Going fullscreen (reveal's own 'f' shortcut) is what a presenter
  // already does before presenting to an audience, so it doubles as the
  // signal for free. In a NOTES iframe (inside the speaker-view popup),
  // fullscreen is read from the actual MAIN window via window.opener,
  // since that's the window that matters (the audience-facing display) --
  // the speaker-view popup itself is not expected to go fullscreen.
  function isPresenting() {
    if (windowType === 'MAIN') {
      return !!document.fullscreenElement;
    }
    try {
      return !!(window.parent && window.parent.opener && window.parent.opener.document.fullscreenElement);
    } catch (e) {
      return false;
    }
  }

  // Send the pointer state
  function broadcastPointer(coords, type) {
    const message = {
      namespace: 'reveal-pointer-sync',
      type: type,
      from: windowType,
      relX: coords ? coords.relX : 0,
      relY: coords ? coords.relY : 0,
    };
    
    // Send a message to the NOTES view (from MAIN)
    if (windowType === 'MAIN' && speakerWindow && !speakerWindow.closed) {
      if (currentSlideWindow) {
        currentSlideWindow.postMessage(JSON.stringify(message), '*');
      }
    }
    
    // Send a message to the MAIN window (from NOTES)
    if (windowType === 'NOTES' && window.parent.opener) {
      window.parent.opener.postMessage(JSON.stringify(message), '*');
    }
  }

  // update the current-slide window in NOTES
  function updateNotesIframeWindow(event) {
    if (currentSlideWindow !== event.source) {
      currentSlideWindow = event.source;
    }
  }
  
  function setKeepAlive(windowType) {
    // Notify the iframe window of current
    //
    // Quick hack: The speaker view contains two iframes: one for the current slide
    // and one for the upcoming slide. They have the same contents, but display
    // different slides.
    // I couldn't find a reliable way to distinguish them from inside the iframe,
    // so as a workaround, I use `postMessageEvents=true` to detect the current slide,
    // since the upcoming one doesn't have this parameter.
    if (windowType === 'NOTES' && window.location.search.includes('postMessageEvents=true')) {
      const message = {
        namespace: 'reveal-pointer-sync',
        type: 'keepalive',
        from: windowType
      }
      const intervalId = setInterval(() => {
        window.parent.opener.postMessage(JSON.stringify(message), '*');
      }, 1000);
    }
  }

  return {
    id: 'RevealPointerSync',
    init: (deck) => {
      pointer = createPointer();
      
      console.log('========================================');
      console.log(`[${windowType}] RevealPointerSync Plugin initialized`);
      console.log('========================================');
      
      // Message listener
      window.addEventListener('message', (event) => {
        let data = event.data;
        
        if (typeof data === 'string') {
          try {
            data = JSON.parse(data);
          } catch (e) {
            return;
          }
        }
        
        // Obtain the window reference from reveal-notes
        if (data && data.namespace === 'reveal-notes') {
          if (event.source && event.source !== window) {
            speakerWindow = event.source;
            // console.log(`[${windowType}] ✅ Speaker view captured`);
          }
        }
        
        // Processing the reveal-pointer-sync messages
        if (data && data.namespace === 'reveal-pointer-sync') {
          if (data.type === 'move') {
            const actual = getActualCoordinates(data.relX, data.relY);
            if (actual) {
              // Render the pointer based on its coordinates and size
              showPointer(actual.x, actual.y, actual.size);
            }
          } else if (data.type === 'hide') {
            hidePointer();
          } else if (data.type === 'keepalive') {
            updateNotesIframeWindow(event);
          }
        }
      });
      
      // Mouse movement event -- shows the pointer while the mouse is over
      // the slide area AND the deck is actually in fullscreen (see
      // isPresenting() above). Every key-based toggle we tried (Alt+P,
      // Shift+P, F8) ran into something on the presenter's machine
      // intercepting the keystroke before the page ever saw it (Vimium, a
      // WM binding, a 2FA autotype tool...), and the disable toggle itself
      // had its own bug distributing state across the speaker view's
      // multiple windows/iframes. Fullscreen has no key to intercept and
      // no state to get out of sync.
      document.addEventListener('pointermove', (event) => {
        const coords = isPresenting() ? getSlideCoordinates(event.clientX, event.clientY) : null;
        if (coords) {
          if (!isPointerActive) {
            isPointerActive = true;
            console.log(`[${windowType}] Pointer ON`);
          }

          // Render in the current window by calculating the current window size
          const actual = getActualCoordinates(coords.relX, coords.relY);
          if (actual) {
            showPointer(event.clientX, event.clientY, actual.size);
          }

          broadcastPointer(coords, 'move');
        } else if (isPointerActive) {
          isPointerActive = false;
          hidePointer();
          broadcastPointer(null, 'hide');
          console.log(`[${windowType}] Pointer OFF (left slide area)`);
        }
      });

      // Hide immediately on leaving fullscreen, rather than waiting for the
      // next mouse move (which might not come until the pointer is already
      // sitting somewhere on top of the now-windowed page).
      if (windowType === 'MAIN') {
        document.addEventListener('fullscreenchange', () => {
          if (!document.fullscreenElement) {
            isPointerActive = false;
            hidePointer();
            broadcastPointer(null, 'hide');
          }
        });
      }

      setKeepAlive(windowType);

      console.log(`[${windowType}] 💡 Press 'S' to open speaker view`);
      console.log(`[${windowType}] 💡 Go fullscreen ('f') and move the mouse over the slide to show the laser pointer`);
    }
  };

})();
