# ⚙️ Industrial Project (Mini-ERP & Maintenance System)

A **Mini-ERP** web application developed in **Python and Django**, specially designed for industrial and manufacturing environments. The project simulates real-world factory workflows, integrating inventory management, spare parts requisition flows, equipment status control, automation error (PLC) diagnostics, and analytical reports generated via **MATLAB**.

---

## 🚀 Key Features

### 1. Dispatcher Portal (Operator Portal)
* **Inventory View**: Real-time monitoring of current stock levels and minimum alert thresholds for parts and materials.
*
<img width="963" height="1018" alt="image" src="https://github.com/user-attachments/assets/21ab02a4-61e9-44b8-9384-66f13e56feb8" />

### 2. Manager / Chief Engineer Dashboard
* **Secure Authentication**: Restricted access based on a dedicated username and password for decision-making personnel.
<img width="957" height="1017" alt="image" src="https://github.com/user-attachments/assets/1946725c-4e92-4489-bc58-292a34b05ddc" />

* **Approve / Reject Requisitions**: Validation of parts requests with automatic and secure stock deduction from inventory.
* **Equipment Monitoring & Control**: Tracking the status of production lines (Operational / Under Maintenance or Stopped).
* **PLC Error & Fault Module**: Recording error codes and descriptions when equipment is stopped, facilitating rapid troubleshooting.
* **MATLAB Analytical Reports**: Automatic visualization of stock charts generated directly from the application database via MATLAB scripts.
<img width="956" height="1019" alt="image" src="https://github.com/user-attachments/assets/ce81a92a-1494-4ff3-b498-172ce7b7d90c" />
<img width="959" height="1019" alt="image" src="https://github.com/user-attachments/assets/1c5bbe6d-1316-43fe-bb43-e3fcfc98e49c" />

### 3. Modern Industrial Design
* Clean and responsive interface built with **Bootstrap 5**, using a professional theme based on industrial blue and steel gray.

---

## 🛠️ Tech Stack

* **Backend**: Python, Django (Models, Views, Templates, Authentication)
* **Data Analysis & Reporting**: MATLAB (SQLite Connection & `.png` Chart Generation)
* **Frontend**: HTML5, Bootstrap 5, Custom CSS
* **Database**: SQLite
