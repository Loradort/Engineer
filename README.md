# Engineer

```mermaid
erDiagram

EngineerType {
    name char PK
}

Engineer {
    type char FK
    fname char
    lname char
}

Building {
    B_name char PK
}

Room {
    room_no int
    building char FK
}

Room {
    engineer char FK
    room char FK
    detail text
    status int
    created_at datetime
    updated_at datetime
}
Room ||--|| Building : "have"
Building ||--|| Engineer "asd"
Engineertype ||--|| Engineer : "has"
Room ||--|| Engineer || : "to"

```

### EngineerType
| Field | Type | Domain | Key |
| ---   |  --- |  ---   | --- |
|name | char | 255 | PK |

### Engineer
| Field | Type | Domain | Key |
| ---   |  --- |  ---   | --- |
|type | () | () | FK |
|fname | char | 255 | |
|lname | char | 255 | |

### Building
| Field | Type | Domain | Key |
| ---   |  --- |  ---   | --- |
|B_name | char | () | PK |

### Room
| Field | Type | Domain | Key |
| ---   |  --- |  ---   | --- |
|room_no | int | () |  |
|building | () | () | FK |

### Assignment
| Field | Type | Domain | Key |
| ---   |  --- |  ---   | --- |
|engineer | () | () | FK |
|room | () | () | FK |
|detail | text | () | |
|status| int | () |  |
|created_at | date |  | |
|updated_at | date |  | |

