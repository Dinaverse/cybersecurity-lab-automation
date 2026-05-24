# Cybersecurity Lab Automation

## Description
Suite d'agents autonomes et scripts d'analyse pour la cybersécurité. Automatise la surveillance de logs et la reconnaissance réseau.

## Contenu
- Agents d'analyse (Security-Ops, Net-Analyzer)
- Scripts de détection d'anomalies
- Pont d'intégration MCP

## Utilisation
Les agents sont conçus pour fonctionner en tant que services d'arrière-plan sur le cluster de calcul.

## Résolution des problèmes (MCP Server)
Voir [Documentation détaillée](docs/MCP_SECURITY_FIX.md) pour la solution complète.
*   **Problème :** Échec de communication/initialisation du serveur MCP.
*   **Solution :** Vérification de la configuration TypeScript, validation des permissions d'exécution des binaires du serveur, et synchronisation des chemins dans le registre des outils ().
