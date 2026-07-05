# 🚨 Sannidhi Error Code Specification

> **Version:** 1.0
> **Project:** Sannidhi
> **Purpose:** Standardized application-level error codes for all services, APIs, plugins, and modules.

---

# 📖 Overview

Sannidhi uses **two layers of errors**:

1. **HTTP Status Codes** (Standard)
2. **Application Error Codes** (Custom)

Example:

```json
{
    "error_code": "AUTH_001",
    "message": "Invalid email or password.",
    "request_id": "6afdb02b-a25d-45c7-9d5d-b69fca9d2a3e"
}
```

---

# 🏗 Error Code Naming Convention

```
MODULE_ERRORNUMBER
```

Examples:

```
AUTH_001
TENANT_003
USER_008
CONFIG_002
PLUGIN_004
```

Advantages:

* Human readable
* Easy to search in logs
* Stable for frontend applications
* Independent of error messages

---

# 📂 Module Prefixes

| Prefix     | Module             |
| ---------- | ------------------ |
| AUTH       | Authentication     |
| USER       | User Management    |
| TENANT     | Multi-Tenancy      |
| ATTENDANCE | Attendance         |
| GEOFENCE   | Geofence           |
| LEAVE      | Leave Management   |
| REPORT     | Reports            |
| CONFIG     | Configurations     |
| PLUGIN     | Plugins            |
| EMAIL      | Email Service      |
| API        | API Keys           |
| SECURITY   | Security           |
| VALIDATION | Request Validation |
| CACHE      | Cache              |
| DB         | Database           |
| SYSTEM     | Internal System    |
| LOG        | Logging            |
| TRACE      | Observability      |

---

# 🔐 Authentication

| Code     | Description                        |
| -------- | ---------------------------------- |
| AUTH_001 | Invalid credentials                |
| AUTH_002 | User not found                     |
| AUTH_003 | User already exists                |
| AUTH_004 | Account disabled                   |
| AUTH_005 | Account locked                     |
| AUTH_006 | Invalid JWT token                  |
| AUTH_007 | JWT expired                        |
| AUTH_008 | Refresh token expired              |
| AUTH_009 | Invalid refresh token              |
| AUTH_010 | Email not verified                 |
| AUTH_011 | Invalid OTP                        |
| AUTH_012 | OTP expired                        |
| AUTH_013 | Invalid password reset token       |
| AUTH_014 | Password reset token expired       |
| AUTH_015 | Multi-factor authentication failed |

---

# 👤 User Management

| Code     | Description               |
| -------- | ------------------------- |
| USER_001 | User not found            |
| USER_002 | User already exists       |
| USER_003 | Invalid role              |
| USER_004 | User inactive             |
| USER_005 | User suspended            |
| USER_006 | Password mismatch         |
| USER_007 | Password policy violation |
| USER_008 | Email already registered  |
| USER_009 | Username already exists   |

---

# 🏢 Multi-Tenant

| Code       | Description                  |
| ---------- | ---------------------------- |
| TENANT_001 | Tenant not found             |
| TENANT_002 | Tenant already exists        |
| TENANT_003 | Tenant inactive              |
| TENANT_004 | Invalid tenant               |
| TENANT_005 | Tenant suspended             |
| TENANT_006 | Tenant limit exceeded        |
| TENANT_007 | Subscription expired         |
| TENANT_008 | Invalid tenant identifier    |
| TENANT_009 | Tenant configuration missing |

---

# 📍 Geofence

| Code         | Description              |
| ------------ | ------------------------ |
| GEOFENCE_001 | Geofence not found       |
| GEOFENCE_002 | Duplicate geofence       |
| GEOFENCE_003 | Invalid coordinates      |
| GEOFENCE_004 | Outside allowed geofence |
| GEOFENCE_005 | Invalid radius           |
| GEOFENCE_006 | Geofence disabled        |

---

# 🕒 Attendance

| Code           | Description                 |
| -------------- | --------------------------- |
| ATTENDANCE_001 | Already checked in          |
| ATTENDANCE_002 | Already checked out         |
| ATTENDANCE_003 | Attendance record not found |
| ATTENDANCE_004 | Invalid attendance status   |
| ATTENDANCE_005 | Outside attendance window   |
| ATTENDANCE_006 | Attendance already approved |

---

# 🌴 Leave Management

| Code      | Description                |
| --------- | -------------------------- |
| LEAVE_001 | Leave request not found    |
| LEAVE_002 | Insufficient leave balance |
| LEAVE_003 | Leave already approved     |
| LEAVE_004 | Leave already rejected     |
| LEAVE_005 | Invalid leave dates        |
| LEAVE_006 | Overlapping leave request  |

---

# 📊 Reports

| Code       | Description               |
| ---------- | ------------------------- |
| REPORT_001 | Report generation failed  |
| REPORT_002 | Invalid report type       |
| REPORT_003 | Report not found          |
| REPORT_004 | Export failed             |
| REPORT_005 | Unsupported report format |

---

# ⚙ Configurations

| Code       | Description                  |
| ---------- | ---------------------------- |
| CONFIG_001 | Configuration not found      |
| CONFIG_002 | Invalid configuration        |
| CONFIG_003 | Configuration already exists |
| CONFIG_004 | Configuration update failed  |
| CONFIG_005 | Configuration corrupted      |
| CONFIG_006 | Active configuration missing |

---

# 🔌 Plugins

| Code       | Description                  |
| ---------- | ---------------------------- |
| PLUGIN_001 | Plugin not found             |
| PLUGIN_002 | Plugin disabled              |
| PLUGIN_003 | Plugin installation failed   |
| PLUGIN_004 | Invalid plugin configuration |
| PLUGIN_005 | Plugin version mismatch      |
| PLUGIN_006 | Missing plugin dependency    |

---

# 📧 Email

| Code      | Description                |
| --------- | -------------------------- |
| EMAIL_001 | Email provider unavailable |
| EMAIL_002 | Failed to send email       |
| EMAIL_003 | Invalid SMTP credentials   |
| EMAIL_004 | Email template missing     |
| EMAIL_005 | Email provider timeout     |

---

# 🔑 API Keys

| Code    | Description        |
| ------- | ------------------ |
| API_001 | API key missing    |
| API_002 | Invalid API key    |
| API_003 | API key expired    |
| API_004 | API key revoked    |
| API_005 | API quota exceeded |

---

# 🛡 Security

| Code         | Description                  |
| ------------ | ---------------------------- |
| SECURITY_001 | Unauthorized request         |
| SECURITY_002 | Forbidden request            |
| SECURITY_003 | CSRF validation failed       |
| SECURITY_004 | Rate limit exceeded          |
| SECURITY_005 | Suspicious activity detected |
| SECURITY_006 | IP address blocked           |
| SECURITY_007 | Invalid request signature    |

---

# ✅ Validation

| Code           | Description             |
| -------------- | ----------------------- |
| VALIDATION_001 | Required field missing  |
| VALIDATION_002 | Invalid request payload |
| VALIDATION_003 | Invalid data type       |
| VALIDATION_004 | Invalid date            |
| VALIDATION_005 | Invalid email format    |
| VALIDATION_006 | Invalid phone number    |

---

# ⚡ Cache

| Code      | Description           |
| --------- | --------------------- |
| CACHE_001 | Cache unavailable     |
| CACHE_002 | Cache miss            |
| CACHE_003 | Failed to write cache |

---

# 🗄 Database

| Code   | Description                   |
| ------ | ----------------------------- |
| DB_001 | Database unavailable          |
| DB_002 | Record not found              |
| DB_003 | Duplicate record              |
| DB_004 | Transaction failed            |
| DB_005 | Database constraint violation |

---

# 📜 Logging

| Code    | Description             |
| ------- | ----------------------- |
| LOG_001 | Failed to write log     |
| LOG_002 | Log storage unavailable |

---

# 🔍 Observability

| Code      | Description           |
| --------- | --------------------- |
| TRACE_001 | Trace creation failed |
| TRACE_002 | Trace export failed   |

---

# 💻 Internal System

| Code       | Description            |
| ---------- | ---------------------- |
| SYSTEM_001 | Internal server error  |
| SYSTEM_002 | Service unavailable    |
| SYSTEM_003 | Dependency unavailable |
| SYSTEM_004 | Unknown system error   |

---

# 📦 Recommended Exception Structure

```python
class TenantNotFoundError(Exception):
    code = "TENANT_001"
    http_status = 404
    message = "Tenant not found."
```

---

# 🌐 Standard API Error Response

```json
{
    "success": false,
    "error_code": "TENANT_001",
    "message": "Tenant not found.",
    "request_id": "6afdb02b-a25d-45c7-9d5d-b69fca9d2a3e",
    "timestamp": "2026-07-05T10:30:00Z"
}
```

---

# 📋 Design Principles

* Use standard HTTP status codes alongside custom error codes.
* Never rely on error messages in frontend applications.
* Error messages may change; error codes should remain stable.
* Log detailed internal errors, but expose only safe messages to clients.
* Group error codes by module for easier maintenance.
* Include a `request_id` in every error response for traceability.
* Keep codes immutable once released to clients.

---

## © Sannidhi Engineering Guidelines

This document defines the canonical error code registry for the Sannidhi platform. All new modules should follow the established naming convention and register new error codes under the appropriate module prefix.
