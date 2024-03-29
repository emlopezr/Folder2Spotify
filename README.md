# Folder2Spotify

![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![ Terminal](https://img.shields.io/badge/Terminal-%234D4D4D.svg?style=for-the-badge&logo=windows-terminal&logoColor=white)

## Table of Contents / Índice

- [Folder2Spotify](#folder2spotify)
    - [English](#english)
    - [Español](#español)
- [Tutorial](#tutorial)
    - [How to Use (English)](#how-to-use-english)
    - [Cómo Usar (Español)](#cómo-usar-español)

## English

Folder2Spotify is a Python tool that allows you to create Spotify playlists from songs stored in local folders. Say goodbye to manually adding songs to your playlists - Folder2Spotify automates the process for you!

This tool simplifies the process of creating Spotify playlists by converting your local music collection stored in folders into curated playlists on Spotify.

## Español

Folder2Spotify es una herramienta en Python que te permite crear listas de reproducción en Spotify a partir de canciones almacenadas en carpetas locales. Di adiós a agregar manualmente canciones a tus listas de reproducción: ¡Folder2Spotify automatiza el proceso por ti!

Esta herramienta simplifica el proceso de creación de listas de reproducción en Spotify convirtiendo tu colección de música local almacenada en carpetas en listas de reproducción curadas en Spotify.

# Tutorial

## How to Use (English)

### Prerequisites

- Python installed on your system
- A Spotify account
- Spotify client ID and client secret (The proccess will be explained later)

### Installation

1. **Clone this repository to your local machine:**
    ```bash
    git clone https://github.com/emlopezr/Folder2Spotify.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd Folder2Spotify
    ```

### Virtual Environment Setup

1. **Install virtualenv:**
    ```bash
    pip install virtualenv
    ```

2. **Create the Virtual Environment:** Use any of this commands
    ```bash
    python -m venv .venv
    python3 -m venv .venv
    py -m venv .venv
    ```
    This will create a directory named .venv in your project folder containing all the necessary files for your virtual environment.

3. **Activate the Virtual Environment:**
    - Windows: ```.venv\Scripts\activate```
    - Linux / MacOS: ```source .venv/bin/activate```

4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Go to Spotify for Developers Dashboard:** https://developer.spotify.com/dashboard

2. **Create an app to get tokens:**
    ![Screenshot_1](https://github.com/emlopezr/Folder2Spotify/assets/45053254/43dc8ba8-40a9-41bb-80b8-79af9a56c198)
    ![Screenshot_2](https://github.com/emlopezr/Folder2Spotify/assets/45053254/25e71a69-d104-450f-9aee-e6837c4a9d9f)

3. **Get the Client ID and Client secret:**
    ![Screenshot_3](https://github.com/emlopezr/Folder2Spotify/assets/45053254/b3b6a3a5-c0b7-48e7-8e80-81ab5261ba24)
    ![Screenshot_4](https://github.com/emlopezr/Folder2Spotify/assets/45053254/1118f84e-a7ed-4852-a80b-d1bf32c9277b)
    ![Screenshot_5](https://github.com/emlopezr/Folder2Spotify/assets/45053254/4df9c146-a8f5-47dd-b6c4-3c83c82482b4)
    ![Screenshot_1](https://github.com/emlopezr/Folder2Spotify/assets/45053254/33420ffc-8730-45ae-b341-bd840be3f0a9)


4. **Make a folder that contains all the songs:**
    ![Screenshot_2](https://github.com/emlopezr/Folder2Spotify/assets/45053254/0cc0896d-f5c3-4a77-9793-f3510d723f04)


5. **Run the Python program:** Use any of this commands
    ```bash
    python main.py
    python3 main.py
    py main.py
    ```

## Cómo Usar (Español)

### Requisitos Previos

- Python instalado en tu sistema
- Una cuenta de Spotify
- ID de cliente y clave secreta de cliente de Spotify (El proceso se explicará más adelante)

### Instalación

1. **Clona este repositorio en tu máquina local:**
    ```bash
    git clone https://github.com/emlopezr/Folder2Spotify.git
    ```

2. **Navega al directorio del proyecto:**
    ```bash
    cd Folder2Spotify
    ```

### Configuración del Entorno Virtual

1. **Instala virtualenv:**
    ```bash
    pip install virtualenv
    ```

2. **Crea el Entorno Virtual:** Utiliza alguno de estos comandos
    ```bash
    python -m venv .venv
    python3 -m venv .venv
    py -m venv .venv
    ```
    Esto creará un directorio llamado .venv en la carpeta de tu proyecto que contendrá todos los archivos necesarios para tu entorno virtual.

3. **Activa el Entorno Virtual:**
    - Windows: ```.venv\Scripts\activate```
    - Linux / MacOS: ```source .venv/bin/activate```

4. **Instala las Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

### Uso

1. **Ve al Panel de Control de Spotify para Desarrolladores:** [https://developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)

2. **Crea una aplicación para obtener tokens:**
    ![Screenshot_1](https://github.com/emlopezr/Folder2Spotify/assets/45053254/43dc8ba8-40a9-41bb-80b8-79af9a56c198)
    ![Screenshot_2](https://github.com/emlopezr/Folder2Spotify/assets/45053254/25e71a69-d104-450f-9aee-e6837c4a9d9f)

3. **Obtén el ID de Cliente y la Clave Secreta de Cliente:**
    ![Screenshot_3](https://github.com/emlopezr/Folder2Spotify/assets/45053254/b3b6a3a5-c0b7-48e7-8e80-81ab5261ba24)
    ![Screenshot_4](https://github.com/emlopezr/Folder2Spotify/assets/45053254/1118f84e-a7ed-4852-a80b-d1bf32c9277b)
    ![Screenshot_5](https://github.com/emlopezr/Folder2Spotify/assets/45053254/4df9c146-a8f5-47dd-b6c4-3c83c82482b4)
    ![Screenshot_1](https://github.com/emlopezr/Folder2Spotify/assets/45053254/33420ffc-8730-45ae-b341-bd840be3f0a9)

4. **Crea una carpeta que contenga todas las canciones:**
    ![Screenshot_2](https://github.com/emlopezr/Folder2Spotify/assets/45053254/0cc0896d-f5c3-4a77-9793-f3510d723f04)

5. **Ejecuta el programa Python:** Utiliza alguno de estos comandos
    ```bash
    python main.py
    python3 main.py
    py main.py
    ```
