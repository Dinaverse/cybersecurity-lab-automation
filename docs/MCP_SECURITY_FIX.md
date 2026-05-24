# Problème : Configuration peu fiable des outils MCP

La configuration précédente reposait sur `npx` pour récupérer et exécuter des paquets de serveurs MCP individuels pour divers outils de sécurité (ex: nmap, sqlmap, metasploit). Cette approche était fondamentalement défaillante pour les raisons suivantes :
1. Beaucoup de ces paquets n'existaient pas dans le registre npm (erreurs 404), provoquant des échecs immédiats au démarrage.
2. Ceux qui existaient souffraient de problèmes de résolution de modules (`ERR_MODULE_NOT_FOUND`) dus à des dépendances instables et à un manque de maintenance.
3. La gestion de chaque outil comme un paquet `npx` indépendant créait un environnement extrêmement fragmenté et fragile.

# Solution : Architecture Docker conteneurisée

J'ai mis en place une architecture centralisée basée sur Docker pour remplacer ces dépendances défaillantes :
1. **Serveur MCP personnalisé :** Création de `mcp-security-server.ts` (compilé vers `/home/dina/dist/mcp-security-server.js`), servant de couche d'orchestration unifiée.
2. **Exécution éphémère :** Le serveur utilise `dockerode` pour exécuter dynamiquement les outils de sécurité dans des conteneurs Docker éphémères (`docker run --rm`), garantissant l'isolation et la répétabilité.
3. **Mappage standardisé :** Tous les outils de sécurité demandés ont été mappés sur des images Docker stables et maintenues (ex: `instrumentisto/nmap`, `projectdiscovery/nuclei`) dans la configuration du serveur.
4. **Configuration simplifiée :** Toutes les entrées individuelles et défectueuses des outils dans `claude_desktop_config.json` ont été remplacées par une référence unique et fiable au nouveau serveur MCP `security-tools`.

Cette architecture garantit une grande fiabilité et facilite la maintenance de la suite d'outils de sécurité sans avoir à gérer des dizaines de paquets npm indépendants.
