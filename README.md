# ⚙️ Proiect Industrial (Mini-ERP & Maintenance System)

O aplicație web de tip **Mini-ERP** dezvoltată în **Python și Django**, concepută special pentru mediul industrial și de producție. Proiectul simulează fluxurile reale dintr-o fabrică, integrând gestionarea stocurilor, fluxul de cereri pentru piese de schimb (*requisitions*), controlul stării utilajelor, diagnosticarea erorilor de automatizare (PLC) și rapoarte analitice generate prin **MATLAB**.

---

## 🚀 Caracteristici Principale

### 1. Portal Dispecer (Operator Portal)
* **Vizualizare Inventar**: Monitorizarea în timp real a stocurilor curente și a pragurilor minime de alertă pentru piese și materiale.
* **Plasare Cereri (Requisitions)**: Crearea de cereri de materiale asociate direct cu departamentul solicitant și cu **utilajul sau linia de producție** care necesită intervenție.
<img width="963" height="1018" alt="image" src="https://github.com/user-attachments/assets/21ab02a4-61e9-44b8-9384-66f13e56feb8" />

### 2. Panou Manager / Inginer Șef
* **Autentificare Securizată**: Acces restricționat pe bază de cont și parolă dedicată pentru personalul de decizie.
<img width="957" height="1017" alt="image" src="https://github.com/user-attachments/assets/1946725c-4e92-4489-bc58-292a34b05ddc" />

* **Aprobare / Respingere Cereri**: Validarea cererilor de piese cu scădere automată și sigură a stocului din inventar.
* **Monitorizare și Control Utilaje**: Urmărirea stării liniilor de producție (Funcțional / În Mentenanță sau Oprit).
* **Modul de Erori și Avarii PLC**: Înregistrarea codurilor și descrierilor de erori în momentul opririi unui utilaj, facilitând diagnosticarea rapidă.
* **Rapoarte Analitice MATLAB**: Vizualizarea automată a graficelor de stocuri generate direct din baza de date a aplicației prin scripturi de MATLAB.
<img width="956" height="1019" alt="image" src="https://github.com/user-attachments/assets/ce81a92a-1494-4ff3-b498-172ce7b7d90c" />
<img width="959" height="1019" alt="image" src="https://github.com/user-attachments/assets/1c5bbe6d-1316-43fe-bb43-e3fcfc98e49c" />

### 3. Design Industrial Modern
* Interfață curată și responsivă realizată cu **Bootstrap 5**, folosind o temă profesională bazată pe albastru industrial și gri oțel.

---

## 🛠️ Stack Tehnologic

* **Backend**: Python, Django (Models, Views, Templates, Authentication)
* **Analiză de Date & Raportare**: MATLAB (Conexiune SQLite & Generare Grafice `.png`)
* **Frontend**: HTML5, Bootstrap 5, CSS personalizat
* **Bază de date**: SQLite
