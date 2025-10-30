@echo off
color a
title Nettoyage de dossier
echo ==============================
echo      MENU DE NETTOYAGE
echo ==============================
color 6
echo 1. Clean Project
color c
echo 2. Clean Simulation
echo.
color a
set /p choice="Entrez votre choix (1 ou 2) : "

REM Définition des dossiers
set "SIM_FOLDER=D:\Projet\F1-Simulation\simulation"
set "GOOD_SIM_FOLDER=D:\Projet\F1-Simulation\good_sim"

if "%choice%"=="1" (
    echo Nettoyage des dossiers Simulation et Good_Sim...
    if exist "%SIM_FOLDER%" del /q "%SIM_FOLDER%\*.*"
    if exist "%GOOD_SIM_FOLDER%" del /q "%GOOD_SIM_FOLDER%\*.*"
    color f
    goto end
)

if "%choice%"=="2" (
    echo Nettoyage du dossier Simulation...
    if exist "%SIM_FOLDER%" del /q "%SIM_FOLDER%\*.*"
    color f
    goto end
)
color f
echo Choix invalide.
goto end

:end
pause
