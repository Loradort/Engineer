# Engineer





### EngineerType
| Field | Type | Domain | Key |
| ---   |  --- |  ---   | --- |
|name | char | 255 | PK |

### Engineer
| Field | Type | Domain | Key |
| ---   |  --- |  ---   | --- |
|type | char | () | FK |
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
|building | char | () | FK |

### Engineer
| Field | Type | Domain | Key |
| ---   |  --- |  ---   | --- |
|engineer | char | () | FK |
|room | char | () | FK |
|detail | text | () | |
|status| int | () |  |
|created_at | date |  | |
|updated_at | date |  | |

