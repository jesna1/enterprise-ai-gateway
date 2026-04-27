graph LR
    subgraph Client_Layer [Mobile Client]
        A[Flutter App]
    end

    subgraph Middleware_Layer [Python Gateway]
        B[FastAPI Server]
        C[Pydantic Models]
    end

    subgraph Data_Layer [Enterprise ERP]
        D[Odoo XML-RPC API]
        E[(PostgreSQL)]
    end

    A -- "REST (JSON)" --> B
    B -- "Validation" --> C
    B -- "XML-RPC" --> D
    D <--> E
