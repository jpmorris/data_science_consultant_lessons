# Chrome Extension Architecture — Shopping Assistant

## Key Files

| File | Purpose |
|---|---|
| [`manifest.json`](~/code/recipe-management/shopping-assistant/manifest.json:1) | Extension declaration — permissions, entry points |
| [`manifest.json:6`](~/code/recipe-management/shopping-assistant/manifest.json:6) | `permissions` block |
| [`manifest.json:11`](~/code/recipe-management/shopping-assistant/manifest.json:11) | `host_permissions` — Walmart, Instacart, Amazon |
| [`background.js`](~/code/recipe-management/shopping-assistant/background.js:1) | Service worker — opens side panel on icon click |
| [`sidepanel.js:1`](~/code/recipe-management/shopping-assistant/sidepanel.js:1) | State object |
| [`sidepanel.js:9`](~/code/recipe-management/shopping-assistant/sidepanel.js:9) | `save()` — `chrome.storage.local.set` |
| [`sidepanel.js:13`](~/code/recipe-management/shopping-assistant/sidepanel.js:13) | `load()` — `chrome.storage.local.get` |
| [`sidepanel.js:25`](~/code/recipe-management/shopping-assistant/sidepanel.js:25) | `buildSearchUrl()` — detects Walmart / Instacart / Amazon |
| [`sidepanel.js:78`](~/code/recipe-management/shopping-assistant/sidepanel.js:78) | `chrome.tabs.query` — reads current tab URL |
| [`sidepanel.js:86`](~/code/recipe-management/shopping-assistant/sidepanel.js:86) | `chrome.tabs.update` — navigates to search URL |

---

## Component Overview

```mermaid
graph TD
    subgraph Extension["Chrome Extension"]
        Manifest["manifest.json\ndeclares permissions,\nentry points, host rules"]
        BG["background.js\nservice worker\npersistent event listener"]
        SP["sidepanel.html + sidepanel.js\nvisible UI"]
    end

    subgraph ChromeAPIs["Chrome APIs"]
        TabsAPI["chrome.tabs\nquery active tab\nnavigate tab URL"]
        StorageAPI["chrome.storage.local\npersist shopping list state"]
        PanelAPI["chrome.sidePanel\nopen/close panel"]
        ActionAPI["chrome.action\ntoolbar icon click event"]
    end

    Browser["Active Browser Tab\nWalmart / Instacart / Amazon"]
    User["User"]

    User -->|"clicks extension icon"| ActionAPI
    ActionAPI --> BG
    BG -->|"sidePanel.open()"| PanelAPI
    PanelAPI --> SP

    SP -->|"read/write state"| StorageAPI
    SP -->|"query current tab URL"| TabsAPI
    TabsAPI -->|"tabs.update(searchUrl)"| Browser
```

---

## Shopping Flow (Sequence)

```mermaid
sequenceDiagram
    participant User
    participant SidePanel as sidepanel.js
    participant Storage as chrome.storage.local
    participant Tabs as chrome.tabs
    participant Site as Walmart / Instacart / Amazon

    Note over User,SidePanel: First open
    User->>SidePanel: pastes grocery list, clicks Start
    SidePanel->>SidePanel: parse items into state[]
    SidePanel->>Storage: save state
    SidePanel->>Tabs: query active tab URL
    Tabs-->>SidePanel: current tab URL
    SidePanel->>SidePanel: buildSearchUrl(url, item[0])
    SidePanel->>Tabs: tabs.update(searchUrl)
    Tabs->>Site: navigate to search results

    Note over User,SidePanel: Step through list
    User->>SidePanel: clicks "Added → Next"
    SidePanel->>SidePanel: mark item added, advance index
    SidePanel->>Storage: save state
    SidePanel->>Tabs: tabs.update(next search URL)
    Tabs->>Site: navigate to next item search

    Note over User,SidePanel: Close and reopen panel
    User->>SidePanel: reopens side panel
    SidePanel->>Storage: load state
    Storage-->>SidePanel: saved items + current index
    SidePanel->>SidePanel: render — list restored
```

---

## Extension Contexts Compared

```mermaid
graph TD
    subgraph SW["Service Worker — background.js"]
        direction LR
        E1["Runs persistently in background"]
        E2["No DOM access"]
        E3["Listens to Chrome events:\naction.onClicked\ntabs.onUpdated\nruntime.onMessage"]
    end

    subgraph UI["Side Panel — sidepanel.js"]
        direction LR
        U1["Runs only when panel is open"]
        U2["Full DOM access"]
        U3["Can use all chrome.* APIs"]
        U4["State: chrome.storage (persists)\nnot window.localStorage (lost on close)"]
    end

    subgraph CS["Content Script (not used here)"]
        direction LR
        C1["JS injected into web pages"]
        C2["Can read/modify page DOM"]
        C3["Isolated JS context from page"]
    end

    Manifest["manifest.json\ndeclares all three"]
    Manifest --> SW
    Manifest --> UI
    Manifest --> CS
```
