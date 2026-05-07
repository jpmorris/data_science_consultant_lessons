# Express App Architecture — Recipe Planner

## Key Files

| File | Purpose |
|---|---|
| [`server.js`](~/code/recipe-management/planner/server.js:1) | Entry point — all routes and middleware |
| [`server.js:10`](~/code/recipe-management/planner/server.js:10) | Middleware: `express.json()` + `express.static()` |
| [`server.js:24`](~/code/recipe-management/planner/server.js:24) | `GET /api/recipes` |
| [`server.js:42`](~/code/recipe-management/planner/server.js:42) | `GET /api/past-plans` |
| [`server.js:58`](~/code/recipe-management/planner/server.js:58) | `POST /api/suggest` — Claude meal plan prompt |
| [`server.js:112`](~/code/recipe-management/planner/server.js:112) | `POST /api/save-plan` |
| [`server.js:132`](~/code/recipe-management/planner/server.js:132) | `POST /api/process-ingredients` — Claude ingredient processor |
| [`public/index.html`](~/code/recipe-management/planner/public/index.html:1) | Frontend UI (vanilla JS, no React) |

---

## Component Overview

```mermaid
graph TD
    Browser["Browser\npublic/index.html + vanilla JS"]

    subgraph Express["Express Server — server.js"]
        Static["express.static\nserves public/"]
        R1["GET /api/recipes"]
        R2["GET /api/past-plans"]
        R3["POST /api/suggest"]
        R4["POST /api/save-plan"]
        R5["POST /api/process-ingredients"]
    end

    Sheets["Google Sheets API\nrecipe + plan database"]
    Claude["Claude API\nmeal planner + ingredient processor"]

    Browser -->|"first load — GET /"| Static
    Browser -->|"fetch() API calls"| R1
    Browser -->|"fetch() API calls"| R2
    Browser -->|"fetch() API calls"| R3
    Browser -->|"fetch() API calls"| R4
    Browser -->|"fetch() API calls"| R5

    R1 -->|"read rows"| Sheets
    R2 -->|"read rows"| Sheets
    R3 -->|"LLM prompt"| Claude
    R4 -->|"append row"| Sheets
    R5 -->|"LLM prompt"| Claude
```

---

## Request / Response Flow

```mermaid
sequenceDiagram
    participant Browser
    participant Express
    participant Sheets as Google Sheets
    participant Claude as Claude API

    Note over Browser,Express: Page load
    Browser->>Express: GET /
    Express-->>Browser: public/index.html

    Note over Browser,Express: Load data
    Browser->>Express: GET /api/recipes
    Express->>Sheets: spreadsheets.values.get()
    Sheets-->>Express: rows[]
    Express-->>Browser: JSON recipes[]

    Browser->>Express: GET /api/past-plans
    Express->>Sheets: spreadsheets.values.get()
    Sheets-->>Express: rows[]
    Express-->>Browser: JSON past plans[]

    Note over Browser,Express: Generate meal plan
    Browser->>Express: POST /api/suggest {recipes, pastPlans, constraints}
    Express->>Claude: messages.create(meal plan prompt)
    Claude-->>Express: {proposals: [...]}
    Express-->>Browser: JSON proposals

    Note over Browser,Express: Save chosen plan
    Browser->>Express: POST /api/save-plan {weekOf, plan}
    Express->>Sheets: spreadsheets.values.append()
    Sheets-->>Express: ok
    Express-->>Browser: {ok: true}
```

---

## General Express Request Lifecycle

```mermaid
graph LR
    Req["Incoming HTTP\nRequest"]
    MW1["Middleware\nexpress.json()\nparse body"]
    MW2["Middleware\nexpress.static()\nserve files"]
    Router["Router\nmatch METHOD + path"]
    Handler["Route Handler\nasync (req, res) => {}"]
    Res["HTTP Response\nres.json() / res.send()"]

    Req --> MW1 --> MW2 --> Router --> Handler --> Res
```
