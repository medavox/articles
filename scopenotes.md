This table needs wikifying.

Some scopenotes:

|Code Placement | Public | Internal | Protected | Private |
|---------------|--------|----------|-----------|---------|
|Code in class containing variable’s definition | Access allowed | Access allowed | Access allowed | Access allowed |
|Code in descendant of class containing variable’s definition | Access allowed | Access allowed | Access allowed | Access denied |
| Code in different class in same package as variable’s definition | Access allowed | Access allowed | Access denied | Access denied |
| Code not in same package as variable’s definition | Access allowed | Access denied | Access denied | Access denied |

there we are.