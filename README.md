# Sora 2 Watermark Remover

Un projet full-stack pour supprimer automatiquement les watermarks d'une vidéo.  
Le frontend est en **React (Vite)** et le backend en **FastAPI** avec traitement vidéo via **OpenCV**.

---

## Fonctionnalités

- Upload d’une vidéo via l’interface web
- Suppression automatique du watermark sur toute la vidéo
- Téléchargement du fichier vidéo traité
- Compatible avec les vidéos MP4

---

## Tech Stack

- **Frontend:** React + Vite
- **Backend:** FastAPI + Uvicorn
- **Vidéo Processing:** OpenCV, NumPy
- **Langage:** Python 3.11, JavaScript (React)

---

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/ton-compte/watermark-remover.git
cd watermark-remover
```
Créer et activer un environnement virtuel :

cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

Installer les dépendances du frontend (Node.js)
cd ../frontend
npm install

Backend (FastAPI)
cd backend
python -m uvicorn main:app --reload --port 8000


Frontend (React)
cd frontend
npm run dev


Structure du projet
watermark-remover/
├── backend/
│   ├── main.py              # FastAPI backend
│   ├── watermark_remover.py # Fonction de suppression du watermark
│   ├── uploads/             # Vidéos uploadées
│   └── outputs/             # Vidéos traitées
└── frontend/
    ├── src/
    │   ├── App.jsx          # Interface React
    │   ├── main.jsx         # Point d'entrée React
    │   └── index.css
    ├── package.json
    └── vite.config.js
