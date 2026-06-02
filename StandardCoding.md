# คู่มือมาตรฐานการเขียนโค้ด Python QT Designer (AI-Readable Format)

## Table of Contents

1. [Naming Conventions Rules](#naming-conventions-rules)
2. [Database Naming Standards](#database-naming-standards)
3. [Form, Module, Class Naming](#form-module-class-naming)
4. [Variable Naming Standards](#variable-naming-standards)
5. [Function and Method Standards](#function-and-method-standards)
6. [Code Pattern Examples](#code-pattern-examples)
7. [Comment Standards](#comment-standards)
8. [Validation Rules](#validation-rules)

---

## Naming Conventions Rules

### UI Widget Naming Pattern (Tkinter/PyQt)

**Rule**: All UI objects must start with lowercase 'o' followed by type abbreviation

**Pattern**: `o[TYPE_ABBR]_[object_name]`
**Regex**: `^o[a-z]{2,3}_[a-z][a-z0-9_]*$`

| Type Code | Full Name      | Pattern Example | Valid Example        |
| --------- | -------------- | --------------- | -------------------- |
| cb        | ComboBox       | `ocb_[name]`    | `ocb_customer_type`  |
| ck        | CheckBox       | `ock_[name]`    | `ock_is_active`      |
| btn       | Button         | `obtn_[name]`   | `obtn_save_data`     |
| dt        | DatePicker     | `odt_[name]`    | `odt_birth_date`     |
| frm       | Frame/GroupBox | `ofrm_[name]`   | `ofrm_customer_info` |
| gd        | Grid/Table     | `ogd_[name]`    | `ogd_product_list`   |
| lbl       | Label          | `olbl_[name]`   | `olbl_customer_name` |
| lb        | ListBox        | `olb_[name]`    | `olb_category_list`  |
| lv        | ListView       | `olv_[name]`    | `olv_order_history`  |
| img       | Image/Canvas   | `oimg_[name]`   | `oimg_product_image` |
| txt       | TextBox/Entry  | `otxt_[name]`   | `otxt_customer_code` |
| tv        | TreeView       | `otv_[name]`    | `otv_menu_structure` |

### Database Object Naming

**Pattern**: `o[SCOPE]_[TYPE][ABBR]`

| Object Type   | Pattern            | Example     | Description         |
| ------------- | ------------------ | ----------- | ------------------- |
| Connection    | `o[W/XX/VB]_DbCon` | `oW_DbCon`  | Database Connection |
| Adapter       | `o[W/XX/VB]_DbAdt` | `oXX_DbAdt` | Database Adapter    |
| Dataset       | `o[W/XX/VB]_DbDts` | `oVB_DbDts` | Dataset             |
| DataTable     | `o[W/XX/VB]_DbTbl` | `oW_DbTbl`  | DataTable           |
| Command       | `o[W/XX/VB]_DbCmd` | `oXX_DbCmd` | Database Command    |
| DataRow       | `o[W/XX/VB]_Row`   | `oW_Row`    | DataRow             |
| StringBuilder | `o[W/XX/VB]_Sql`   | `oVB_Sql`   | SQL StringBuilder   |

**Scope Codes**:

- `W`: Windows Form scope
- `XX`: Project abbreviation (e.g., SM, PS, RS, CT)
- `VB`: Global/Center scope

---

## Database Naming Standards

### Table Naming Rules

**Pattern**: `T[XX][Y][Name]`
**Regex**: `^T[A-Z]{2}[MTS][A-Za-z]{1,12}$`

**Components**:

- `T`: Fixed prefix for all tables
- `XX`: System abbreviation (2 chars, uppercase)
- `Y`: Table type (1 char)
- `Name`: Table name (max 12 chars)

**System Abbreviations**:
| Code | System | Description |
|------|--------|-------------|
| PS | POS | Point of Sale system |
| FN | Finance | Financial system |
| TK | Ticket | Ticketing system |
| FB | F&B | Food and Beverage |
| CN | Center | Central/Common tables |
| AP | Accounts Payable | AP system |
| AR | Accounts Receivable | AR system |

**Table Type Codes**:
| Code | Type | Description | Example |
|------|------|-------------|---------|
| M | Master | Master data tables | `TCNMPdt` (Product Master) |
| T | Transaction | Transaction/history tables | `TARTSiHD` (Sale Header) |
| S | System | System configuration tables | `TCNSConfig` (System Config) |

### Field Naming Rules

**Pattern**: `F[X][Abc][Name]`
**Regex**: `^F[TDNC][A-Z][a-z]{2}[A-Za-z]{1,10}$`

**Components**:

- `F`: Fixed prefix for all fields
- `X`: Data type code (1 char)
- `Abc`: Table abbreviation (3 chars, PascalCase)
- `Name`: Field name (max 10 chars)

**Data Type Codes**:
| Code | Data Type | C# Type | Example |
|------|-----------|---------|---------|
| T | Text/String | string | `FTBnkCode` |
| D | Date/DateTime | DateTime | `FDBnkRegis` |
| N | Integer/Number | int, long | `FNBnkSeq` |
| C | Currency/Decimal | decimal | `FCBnkAmt` |

**Valid Examples**:

```sql
-- Bank table (TFNMBank)
FTBnkCode     -- Text: Bank Code
FTBnkName     -- Text: Bank Name
FCBnkAmt      -- Currency: Bank Amount
FDBnkRegis    -- Date: Registration Date
FNBnkSeq      -- Number: Sequence Number
```

---

## View, Module, Class Naming

### Form or View or Ui Naming

**Pattern**: `w[Name]`
**Regex**: `^w[A-Z][a-zA-Z0-9]*$`
**Examples**: `wCompany`, `wCustomerList`, `wProductEntry`
**File Name**: `wCompany.ui`, `wCustomerList.ui`, `wProductEntry.ui`

### Module Naming

**Pattern**: `m[XX][YY]`
**Regex**: `^m[A-Z]{2}[A-Z]{2}$`
**Examples**: `mCNSP`, `mCTSP`, `mPSSP`
**File Name**: `mCNSP.py`, `mCTSP.py`, `mPSSP.py`

### Class Naming Rules

#### Model Classes (with get/set)

**Pattern**: `cml[Name]`
**Regex**: `^cml[A-Z][a-zA-Z0-9]*$`
**Examples**: `cmlCustomer`, `cmlProduct`, `cmlUser`
**File Name**: `cmlCustomer.py`, `cmlProduct.py`, `cmlUser.py`

#### Regular Classes

**Pattern**: `c[Name]`
**Regex**: `^c[A-Z][a-zA-Z0-9]*$`
**Examples**: `cCustomer`, `cProduct`, `cUser`
**File Name**: `cCustomer.py`, `cProduct.py`, `cUser.py`

---

## Variable Naming Standards

### Data Type Prefixes

**Pattern**: `[d][Scope_][Name]`

| Prefix | Data Type        | Python Type    | Example                 |
| ------ | ---------------- | -------------- | ----------------------- |
| t      | Text/String      | string         | `tCustomerName`         |
| n, i   | Number/Integer   | int, long      | `nQuantity`, `iCounter` |
| b      | Boolean          | bool           | `bIsActive`             |
| d      | Date             | DateTime       | `dCreatedDate`          |
| o      | Object           | object, custom | `oCustomer`             |
| v      | Variant          | var            | `vResult`               |
| a      | Array/List       | [], List<>     | `atNames`, `anNumbers`  |
| w      | Form             | Form           | `wMainForm`             |
| c      | Currency/Decimal | decimal        | `cTotalAmount`          |
| x      | Void return      | void           | Used in procedures      |

### Variable Scope Rules

#### Global Variables (Module Level)

**Pattern**: `[dataType]W_[Name]`
**Regex**: `^[tnibovaawcx]W_[A-Z][a-zA-Z0-9]*$`

```python
# Global variables
tW_CompanyName = "Adasoft"
nW_TotalQty = 0
bW_IsConnected = False

# Constants (UPPER_CASE)
G_MAX_RETRY = 3
G_DEFAULT_TIMEOUT = 30
G_API_VERSION = "v1"
```

#### Global Variables in Class

**Pattern**: `[dataType]C_[Name]`
**Regex**: `^[tnibovaawcx]C_[A-Z][a-zA-Z0-9]*$`

```python
class C_Customer:
    tC_CompanyName = "Adasoft"
    nC_TotalQty = 0
    bC_IsConnected = False
```

#### Instance Variables

**Pattern**: `self.[dataType][Name]`
**Regex**: `^[tnibovaawcx][A-Z][a-zA-Z0-9]*$`

```python
class C_Customer:
    def __init__(self):
        self.tCustomerName = ""
        self.nCustomerId = 0
        self.bIsActive = True
```

#### Local Variables

**Pattern**: `[dataType][Name]`
**Regex**: `^[tnibovaawcx][A-Z][a-zA-Z0-9]*$`

```python
def W_DATxProcessOrder():
    tCustomer = "John Doe"
    bCheckStatus = True
    cSubTotal = 0.0

### Array, List, Dict, DataFrame Naming

**Pattern**: `a[dataType][Name]`, `dt[Name]`, `df[Name]`

# Array
atCustomerNames = ["John", "Jane", "Bob"]
anQuantities = [10, 20, 30]

# Dictionaries
dtConfig = {"host": "localhost", "port": 3306}
dtCustomer = {"id": 1, "name": "John"}

# DataFrames (Pandas)
dfSales = pd.DataFrame()
dfProducts = pd.read_csv("products.csv")
```

---

## Function and Method Standards

### Function Naming Pattern

**Pattern**: `[Scope]_[Group][ReturnType][Name]([Parameters])`

#### Windows Form Functions

**Pattern**: `W_[UUU][ReturnType][Name]([Parameters])`
**Regex**: `^W_[A-Z]{3}[xtnibovaawc][A-Z][a-zA-Z0-9]*\([^)]*\)$`

#### Class Functions

**Pattern**: `C_[UUU][ReturnType][Name]([Parameters])`
**Regex**: `^C_[A-Z]{3}[xtnibovaawc][A-Z][a-zA-Z0-9]*\([^)]*\)$`

### Function Group Codes (uuu)

| Code | Purpose  | Description                |
| ---- | -------- | -------------------------- |
| fld  | Folder   | Folder/file operations     |
| tbl  | Table    | Database table operations  |
| dat  | Data     | Data processing            |
| prc  | Process  | Business logic processing  |
| get  | Retrieve | Data retrieval/search      |
| set  | Set      | Data setting/configuration |
| chk  | Check    | Validation/verification    |
| api  | API      | API endpoint handlers      |

### Function Examples with Patterns

#### Void Methods (no return)

```python
// Pattern: W_[UUU]x[Name]()
def W_DatInsertData():
    """Insert data into database"""
    pass

def W_SetConfiguration():
    """Set system configuration"""
    pass

def W_PrcCalculateTotal():
    """Calculate total amount"""
    pass
```

#### Methods with Return Values

```python
// Pattern: W_[UUU][ReturnType][Name]([Parameters])
def W_GetCustomerCount(ptFilter: str) -> int:
    """Get customer count with filter"""
    return 0

def W_CHKValidateData(ptCode: str) -> bool:
    """Validate data by code"""
    return True

def W_GetCustomerName(pnId: int) -> str:
    """Get customer name by ID"""
    return ""
```

#### Class Methods

```python
class C_CustomerService:

    # Instance method
    def C_GetCustomerByID(self, pnCustomerId: int) -> dict:
        """Get customer data by ID"""
        return {}

    # Static method
    @staticmethod
    def C_CHKValidateStock(pnProductId: int) -> bool:
        """Validate product stock"""
        return True

    # Class method
    @classmethod
    def C_GetProductCount(cls, ptCategory: str) -> int:
        """Get product count by category"""
        return 0
```

#### Private Methods

**Pattern**: `_[name]` หรือ `__[name]` (name mangling)

```python
class C_Customer:

    def _validate_email(self, ptEmail: str) -> bool:
        """Private method - validate email"""
        return True

    def __internal_process(self):
        """Private method with name mangling"""
        pass
```

### Parameter Naming

**Pattern**: `p[dataType][Name]`
**Regex**: `^p[tnibovaawcx][A-Z][a-zA-Z0-9]*$`

```python
def W_CHKValidateCustomer(
    ptCustomerCode: str,     # Text parameter
    pnCustomerID: int,       # Number parameter
    pbIsActive: bool,        # Boolean parameter
    pdCreatedDate: datetime  # Date parameter
) -> bool:
    """Validate customer data"""
    return True
```

---

## Code Pattern Examples

### Static Method Pattern

```python
class W_CustomerService:

    @staticmethod
    def W_GETnCalculateTotal(pnValue1: int, pnValue2: int) -> int:
        """Calculate total of two values"""
        nNumber1 = pnValue1
        nNumber2 = pnValue2
        return nNumber1 + nNumber2

    @staticmethod
    def C_PRCbValidateLogin(ptUsername: str, ptPassword: str) -> bool:
        """Validate user login credentials"""
        bResult = False

        # Validation logic here
        if ptUsername and ptPassword:
            bResult = True

        return bResult
```

### Instance Method Pattern

```python
class W_DATxSaveCustomer:

    def __init__(self):
        self.owDBCon = None

    def W_DatSaveCustomer(self, ptCustomerName: str, ptCustomerCode: str) -> None:
        """Save customer data to database"""
        # Save logic here
        if ptCustomerName:
            # Process saving
            pass

    def W_GetCustomerByID(self, pnCustomerID: int) -> str:
        """Get customer name by ID"""
        tResult = ""

        # Retrieval logic here
        # ... database operations

        return tResult
```

### Data Class Pattern (Using dataclass)

```python
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

@dataclass
class cmlCustomer:
    """Customer data model"""
    nCustomerID: int = 0
    tCustomerCode: str = ""
    tCustomerName: str = ""
    dCreatedDate: datetime = None
    bIsActive: bool = True
    cCreditLimit: Decimal = Decimal('0.00')
```

### Data Class Pattern (Traditional Class)

```python
class cmlCustomer:
    """Customer data model"""

    def __init__(self):
        self.nCustomerID: int = 0
        self.tCustomerCode: str = ""
        self.tCustomerName: str = ""
        self.dCreatedDate: datetime = None
        self.bIsActive: bool = True
        self.cCreditLimit: Decimal = Decimal('0.00')
```

### FastAPI/Flask API Pattern

```python
from fastapi import APIRouter
from typing import Dict, Any

router = APIRouter()

class cmlApiResponse:
    """API response model"""
    def __init__(self):
        self.tCode: str = ""
        self.tMessage: str = ""
        self.oData: Any = None

@router.post("/create")
def C_PostCreateCustomer(poCustomer: cmlCustomer) -> Dict[str, Any]:
    """Create new customer via API"""
    oResult = cmlApiResponse()

    try:
        # Business logic here
        oResult.tCode = "200"
        oResult.tMessage = "Success"
        oResult.oData = poCustomer
    except Exception as ex:
        oResult.tCode = "500"
        oResult.tMessage = str(ex)

    return {
        "code": oResult.tCode,
        "message": oResult.tMessage,
        "data": oResult.oData
    }
```

### Database Connection Pattern

```python
import mysql.connector
from typing import Optional

class C_DatabaseHelper:
    """Database helper class"""

    def __init__(self):
        self.owDBCon: Optional[mysql.connector.connection.MySQLConnection] = None

    def C_DatConnect(self, ptHost: str, ptDatabase: str,
                      ptUser: str, ptPassword: str) -> bool:
        """Connect to database"""
        try:
            self.owDBCon = mysql.connector.connect(
                host=ptHost,
                database=ptDatabase,
                user=ptUser,
                password=ptPassword
            )
            return True
        except Exception as ex:
            print(f"Connection error: {ex}")
            return False

    def C_DatClose(self) -> None:
        """Close database connection"""
        if self.owDBCon:
            self.owDBCon.close()
```

### Pandas DataFrame Pattern

```python
import pandas as pd
from typing import Optional

def W_GetSalesData(ptStartDate: str, ptEndDate: str) -> Optional[pd.DataFrame]:
    """Get sales data as DataFrame"""
    dfResult = None

    try:
        # Query database
        tSql = f"""
            SELECT * FROM t_ar_t_sale_hd
            WHERE f_d_slh_date BETWEEN '{ptStartDate}' AND '{ptEndDate}'
        """

        dfResult = pd.read_sql(tSql, owDBCon)

    except Exception as ex:
        print(f"Error: {ex}")

    return dfResult
```

---

## Comment Standards

### New Code Comments

**Pattern**: `# * [DeveloperName] [DD-MM-YY]`

```python
# * PiTee 15-01-25
def W_DatNewFunction():
    """New function implementation"""
    # New implementation here
    pass
```

### Commented Out Code

**Pattern**: `# * Comment code [DeveloperName] [DD-MM-YY]`

```python
# * Comment code PiTee 15-01-25
# Old implementation that was removed
# def w_dat_old_function():
#     # Old code here
#     pass
```

### Function Documentation (Docstring)

**Style**: Google Style หรือ NumPy Style

```python
def C_CHKValidateCustomer(ptCustomerCode: str, ptCustomerName: str) -> bool:
    """
    Validates customer data and returns validation result.

    Args:
        ptCustomerCcode (str): Customer code to validate
        ptCustomerName (str): Customer name to validate

    Returns:
        bool: True if valid, False otherwise

    Raises:
        ValueError: If customer code is empty

    Example:
        >>> c_chk_validate_customer("C001", "John Doe")
        True
    """
    # * PiTee 15-01-25
    if not ptCustomerCode:
        raise ValueError("Customer code cannot be empty")

    return True
```

### Class Documentation

```python
class C_CustomerService:
    """
    Customer service class for managing customer operations.

    This class handles all customer-related business logic including
    CRUD operations, validation, and data processing.

    Attributes:
        ow_db_con: Database connection object
        t_c_table_name (str): Customer table name

    Example:
        >>> service = CustomerService()
        >>> service.c_dat_save_customer("John", "C001")
    """

    def __init__(self):
        """Initialize CustomerService with default values"""
        self.owDBCon = None
        self.tTableName = "t_cn_m_customer"
```

### Inline Comments

```python
def W_PRCCalculateDiscount(cAmount: float, nDiscountPercent: int) -> float:
    """Calculate discount amount"""

    # Validate discount percentage
    if nDiscountPercent < 0 or nDiscountPercent > 100:
        nDiscountPercent = 0

    # Calculate discount (amount * percentage / 100)
    cDiscount = cAmount * (nDiscountPercent / 100)

    # Return final amount after discount
    return cAmount - cDiscount
```

---

## Validation Rules

### Regular Expression Patterns for Validation

#### Table Names

```regex
^T[A-Z]{2}[MTS][A-Za-z]{1,12}$
```

#### Field Names

```regex
^F[TDNC][A-Z][a-z]{2}[A-Za-z]{1,10}$
```

#### Form Names

```regex
^w[A-Z][a-zA-Z0-9]*$
```

#### Class Names

```regex
^c(ml)?[A-Z][a-zA-Z0-9]*$
```

#### Variable Names

```regex
^[tnibovaawcx](W_|C_)?[A-Z][a-zA-Z0-9]*$
```

#### Function Names

```regex
^(W_|C_)[A-Z]{3}[xtnibovaawc][A-Z][a-zA-Z0-9]*$
```

#### Parameter Names

```regex
^p[tnibovaawcx][A-Z][a-zA-Z0-9]*$
```

### Validation Checklist

#### ✅ Valid Examples

```python
// Tables
TCNMCustomer    // ✅ Center Master Customer
TPSSaleHD      // ✅ POS Transaction Sale Header

// Fields
FTCstCode      // ✅ Text Customer Code
FNCstSeq       // ✅ Number Customer Sequence
FCCstCredit    // ✅ Currency Customer Credit

# Variables
tCompanyName = "Adasoft"    # ✅ Global text
cTotalCount = 0             # ✅ Class variable
bIsValid = True               # ✅ Local boolean

# Functions
def W_DatSaveData():                              # ✅ Module procedure
    pass

def C_GetCustomerCount(ptFilter: str) -> int:    # ✅ Class method
    return 0

def W_CHK_ValidateInput(ptValue: str) -> bool:    # ✅ Validation function
    return True
```

#### ❌ Invalid Examples

```python
// Tables
Customer        // ❌ Missing T prefix
TCustomer       // ❌ Missing system code
TCNCustomer     // ❌ Missing type code

// Fields
CstCode         // ❌ Missing F prefix
FCustomerCode   // ❌ Missing data type
FTCustomerCodeExtraLong  // ❌ Name too long

// Variables
CompanyName     // ❌ Missing data type prefix
tcompanyName    // ❌ Wrong case
t_CompanyName   // ❌ Invalid underscore


# Functions
def SaveData():             # ❌ PascalCase not allowed
    pass

def w_SaveData():          # ❌ Wrong case style
    pass

def WSaveData():           # ❌ Missing underscore
    pass
```

### Python-Specific Best Practices

#### Type Hints (Recommended)

```python
from typing import List, Dict, Optional, Union

def W_GetCustomers(
    pnLimit: int = 10,
    ptFilter: Optional[str] = None
) -> List[Dict[str, any]]:
    """Get list of customers with optional filter"""
    aResult: List[Dict[str, any]] = []
    return aResult
```

#### Context Managers

```python
def W_DatProcessFile(ptFilename: str) -> None:
    """Process file with context manager"""
    with open(ptFilename, 'r') as oFile:
        tContent = oFile.read()
        # Process content
```

#### List Comprehensions

```python
def W_GetActiveCustomers(aCustomers: List[dict]) -> List[dict]:
    """Get only active customers"""
    # Use list comprehension
    aActive = [oCust for oCust in aCustomers if oCust.get('bIsActive')]
    return aActive
```

#### Error Handling

```python
def W_DatSaveData(poData: dict) -> bool:
    """Save data with proper error handling"""
    try:
        # Save logic
        return True
    except ValueError as ex:
        print(f"Validation error: {ex}")
        return False
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return False
    finally:
        # Cleanup if needed
        pass
```

### AI Validation Prompt Template

```
Validate this Python code against Adasoft coding standards:

```

Validate this C# code against Adasoft coding standards:

CHECK:

1. Table names: Pattern T[XX][Y][Name] where XX=system, Y=type(M/T/S)
2. Field names: Pattern F[X][Abc][Name] where X=datatype(T/D/N/C)
3. Variables: Pattern [type][scope_]Name where type=(t/n/b/d/o/v/a/w/c/x)
4. Functions: Pattern [W*/C*][UUU][type][Name] where UUU=group
5. Parameters: Pattern p[type][Name]
6. Classes: Pattern c[ml]?[Name]
7. Forms: Pattern w[Name]

REPORT:

- ✅ Compliant items
- ❌ Non-compliant items with corrections
- 📝 Suggestions for improvement

````

---

## Additional Python-Specific Standards

### Import Organization

```python
# Standard library imports
import os
import sys
from datetime import datetime
from typing import List, Dict, Optional

# Third-party imports
import pandas as pd
import numpy as np
from fastapi import FastAPI

# Local application imports
from models.customer import CmlCustomer
from services.database import DatabaseHelper
````

### Constants Definition

```python
# Module-level constants (UPPER_CASE)
G_MAX_RETRY = 3
G_DEFAULT_TIMEOUT = 30
G_API_BASE_URL = "https://api.example.com"
G_ALLOWED_EXTENSIONS = ['.jpg', '.png', '.pdf']
```

### Enum Usage

```python
from enum import Enum

class C_CustomerType(Enum):
    """Customer type enumeration"""
    RETAIL = 1
    WHOLESALE = 2
    VIP = 3
```

### Property Decorators

```python
class C_Customer:
    """Customer class with properties"""

    def __init__(self):
        self._t_name = ""

    @property
    def C_Name(self) -> str:
        """Get customer name"""
        return self._t_name

    @C_Name.setter
    def C_Name(self, ptValue: str) -> None:
        """Set customer name"""
        if not ptValue:
            raise ValueError("Name cannot be empty")
        self._t_name = ptValue
```

---

This Python coding standard maintains consistency with the original C# standards while adapting to Python's conventions and best practices (PEP 8). The naming patterns are preserved but converted to snake_case as per Python standards.
