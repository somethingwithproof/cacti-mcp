<h1 align="center">
	<picture>
		<source media="(prefers-color-scheme: dark)" srcset="../../../images/cacti_mcp_logo_dark.png">
		<img src="../../../images/cacti_mcp_logo.png" width="360" alt="Cacti MCP: a cactus with linked connectors. Connect. Discover. Call.">
	</picture>
</h1>

<p align="center">
	<a href="https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml"><img src="https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml/badge.svg?branch=develop" alt="CI"></a>
	<a href="../../../LICENSE"><img src="https://img.shields.io/badge/license-GPL--2.0--or--later-blue" alt="License: GPL-2.0-or-later"></a>
	<img src="https://img.shields.io/badge/Python-3.12%2B-3776ab?logo=python&amp;logoColor=white" alt="Python 3.12+">
	<img src="https://img.shields.io/badge/MCP-stdio-2e7d32" alt="MCP over stdio">
	<img src="https://img.shields.io/badge/MCP_plugin_API-v2-2e7d32" alt="MCP plugin API v2">
</p>

**Languages:** [English](../../../README.md) · [Deutsch](../de/README.md) · [Español](../es/README.md) · **Français** · [Italiano](../it/README.md) · [Português (BR)](../pt-BR/README.md) · [Nederlands](../nl/README.md) · [Русский](../ru/README.md) · [Українська](../uk/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [简体中文](../zh-CN/README.md) · [繁體中文](../zh-TW/README.md) · [العربية](../ar/README.md) · [हिन्दी](../hi/README.md) · [Polski](../pl/README.md) · [Türkçe](../tr/README.md) · [Svenska](../sv/README.md) · [Tiếng Việt](../vi/README.md) · [Bahasa Indonesia](../id/README.md)

<details><summary>More languages (25 African &amp; Asian locales)</summary>

[Afrikaans](../af-ZA/README.md) · [አማርኛ](../am-ET/README.md) · [العربية (مصر)](../ar-EG/README.md) · [العربية (المغرب)](../ar-MA/README.md) · [বাংলা](../bn/README.md) · [فارسی](../fa/README.md) · [Filipino](../fil/README.md) · [Français (Maroc)](../fr-MA/README.md) · [Français (Sénégal)](../fr-SN/README.md) · [Hausa](../ha-NG/README.md) · [עברית](../he/README.md) · [Igbo](../ig-NG/README.md) · [Malagasy](../mg-MG/README.md) · [मराठी](../mr/README.md) · [Bahasa Melayu](../ms/README.md) · [Kinyarwanda](../rw-RW/README.md) · [Soomaali](../so-SO/README.md) · [Kiswahili](../sw-KE/README.md) · [தமிழ்](../ta/README.md) · [తెలుగు](../te/README.md) · [ไทย](../th/README.md) · [اردو](../ur/README.md) · [isiXhosa](../xh-ZA/README.md) · [Yorùbá](../yo-NG/README.md) · [isiZulu](../zu-ZA/README.md)

</details>

Cacti MCP est un adaptateur Python qui expose les capacités du
[plugin Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) en tant qu'outils MCP
via stdio. Le plugin fournit déjà directement MCP sur HTTP ; utilisez donc
cette option lorsque votre client peut se connecter à un serveur distant. Cet adaptateur est destiné
aux clients qui ne communiquent que via stdio. Il utilise le SDK Python MCP officiel et
traduit les appels d'outils vers l'API HTTPS du plugin (contrat de capacités v2, servi
sous les chemins `/v1/`, jeton bearer uniquement).
Cacti gère l'authentification, l'autorisation, la validation et l'exécution.

**Statut : en cours de développement, avant la version 1.0.** La version 0.1.0 prend en charge
l'inventaire des équipements en lecture seule et les versions de l'installation via le
[plugin Cacti MCP](https://github.com/somethingwithproof/plugin_mcp) compagnon.
Il n'y a pas encore de version taguée. Les diagnostics de type doctor et les réparations feront l'objet de travaux ultérieurs.

## Ce qu'il expose

| Opération | Outil MCP fourni par le plugin Cacti MCP |
|---|---|
| Lister les équipements visibles par le propriétaire du jeton | `cacti-list-devices` |
| Lire un équipement autorisé | `cacti-get-device` |
| Lire les versions de Cacti, du plugin et de l'API | `cacti-get-system-info` |

Les noms, les descriptions et les schémas d'entrée proviennent de la réponse de découverte de Cacti
filtrée par les permissions. D'autres fournisseurs autorisés en lecture seule peuvent être découverts
sans ajouter de gestionnaires d'outils en Python.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Cas d'usage

Connectez un client MCP pour lister les équipements Cacti visibles par son utilisateur dédié,
consulter un équipement autorisé ou récupérer les versions de l'installation lorsque l'utilisateur
dispose du domaine d'administration requis. Les noms et les schémas d'entrée proviennent de
la réponse de découverte du plugin, de sorte que l'adaptateur ne duplique pas chaque fournisseur.
Consultez les
[règles d'enregistrement des capacités](https://github.com/somethingwithproof/plugin_mcp#write-an-ability-plugin-authors)
du plugin pour connaître le modèle d'enregistrement et les limites actuelles.

## Cartographie du code et des tests

| Comportement | Implémentation | Preuves de test dans ce dépôt |
|---|---|---|
| Validation HTTPS, limites, authentification bearer uniquement et pagination v2 | [client.py](../../../src/cacti_mcp/client.py) | [test_client.py](../../../tests/test_client.py) |
| Découverte MCP, appels et changements de permissions | [server.py](../../../src/cacti_mcp/server.py) | [test_stdio.py](../../../tests/test_stdio.py) |
| Aide en ligne de commande, version et configuration manquante | [server.py](../../../src/cacti_mcp/server.py), [__main__.py](../../../src/cacti_mcp/__main__.py) | [test_cli.py](../../../tests/test_cli.py) |

Le test en sous-processus utilise un véritable client et un véritable serveur du SDK avec un point de terminaison HTTP
simulé par fixture. Il ne nécessite ni ne remplace une vérification d'intégration sur un serveur Cacti réel.

## Garanties de sécurité

- Utilise le [SDK Python `mcp` officiel](https://github.com/modelcontextprotocol/python-sdk)
  pour l'initialisation, la découverte d'outils, les appels et le cadrage stdio.
- Expose uniquement les capacités dont les annotations sont exactement en lecture seule, non destructives et idempotentes. Les schémas et les noms proviennent
  de Cacti ; l'adaptateur ne contient ni SQL, ni identifiants d'équipement, ni commandes de réparation.
- Envoie uniquement le jeton bearer : aucun cookie, aucune étape CSRF. Le plugin revérifie
  la validité du jeton et les permissions à chaque requête.
- Utilise HTTPS vérifié, ne stocke jamais de cookies, refuse les redirections et
  ignore les variables d'environnement de proxy. HTTP nécessite `--allow-loopback-http`
  et une adresse de bouclage littérale ou `localhost`.
- Limite les appels API à 35 secondes au total, 5 secondes pour la connexion, 30 secondes
  d'inactivité réseau et environ 1 Mo par réponse (1 100 000 octets).
  Les corps de requête sont limités à 16 384 octets. Les appels sont sérialisés par session
  client.
- Vérifie les arguments d'outils par rapport au schéma d'entrée issu de la dernière découverte avant
  de les envoyer, et exécute uniquement les identifiants issus de ce catalogue vérifié. Une non-conformité, ou
  un schéma malformé renvoyé par le serveur, revient sous forme d'erreur d'outil et non de plantage.
- Ne réessaie pas l'exécution automatiquement. Les erreurs d'outils contiennent uniquement le statut
  HTTP, le `status` AIP-193 et le `reason` ErrorInfo ; jamais de texte de message serveur,
  de corps de réponse ni d'identifiants. Stdout est réservé aux messages MCP.

La version du SDK est figée par `uv.lock` (`mcp>=2.3,<3` dans `pyproject.toml`). Cet
adaptateur utilise son serveur bas niveau 2.x avec le transport stdio ; il n'implémente
pas de point de terminaison MCP HTTP distant, OAuth, les ressources,
les prompts, les abonnements ni les tâches en arrière-plan.

Voir [le contrat d'API](../../../docs/api.md) et [le plan d'implémentation](../../../docs/plan.md).

## Installation et ligne de commande

Nécessite Python 3.12 ou ultérieur et [uv](https://docs.astral.sh/uv/).
Depuis une copie locale de ce dépôt :

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Installez et activez le plugin PHP, accordez son domaine à un utilisateur Cacti dédié,
et créez un jeton d'accès personnel pour cet utilisateur (au format `cmcp_pat_` suivi
de 64 chiffres hexadécimaux en minuscules) dans la console du plugin, sur sa page My MCP Tokens,
ou avec sa commande `tokens.php`.
Les domaines et permissions d'équipement Cacti existants de l'utilisateur continuent de s'appliquer.

Fournissez le jeton via votre gestionnaire de secrets dans `CACTI_MCP_TOKEN` ; ne l'ajoutez jamais
au contrôle de version ni aux arguments de commande. Définissez le point de terminaison séparément. Il doit s'agir d'une
URL HTTPS se terminant par `/plugins/mcp/api.php`, sans identifiants, paramètres de requête ni
fragment :

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

`--endpoint URL` définit le point de terminaison à la place de `CACTI_MCP_ENDPOINT`.
`--allow-loopback-http` autorise le HTTP en clair vers `localhost`, `127.0.0.1` ou `::1`
pour les tests locaux, `--lang LOCALE` remplace la localisation des messages CLI et
`--version` affiche la version. Sans le point de terminaison et `CACTI_MCP_TOKEN`,
la commande se termine avec une erreur d'utilisation.

### Localisation

L'aide de la CLI et les messages d'erreur de l'adaptateur sont fournis en 45 locales (`en`, `de`, `es`, `fr`, `it`, `pt-BR`, `nl`, `ru`, `uk`, `ja`, `ko`, `zh-CN`, `zh-TW`, `ar`, `hi`, `pl`, `tr`, `sv`, `vi`, `id`, `af-ZA`, `am-ET`, `ar-EG`, `ar-MA`, `fr-MA`, `fr-SN`, `ha-NG`, `ig-NG`, `mg-MG`, `rw-RW`, `so-SO`, `sw-KE`, `xh-ZA`, `yo-NG`, `zu-ZA`, `bn`, `fa`, `he`, `mr`, `ta`, `te`, `th`, `ur`, `ms`, `fil`) sans aucune dépendance supplémentaire. La résolution
de la locale vérifie `--lang`, puis `LC_ALL`, `LC_MESSAGES` et `LANG`, avec un repli
sur `en` (`C`/`POSIX` et les balises inconnues se résolvent également vers `en`). Les noms d'outils MCP,
les schémas et les charges utiles JSON des outils réussis ne sont pas affectés ; les messages d'erreur
de l'adaptateur renvoyés avec `is_error=True` suivent la locale active.

Le processus attend des messages MCP sur stdin. Un client MCP le lance normalement.
Pour les clients acceptant le format de configuration courant `mcpServers` :

```json
{
  "mcpServers": {
    "cacti": {
      "command": "uv",
      "args": ["run", "--locked", "--directory", "/absolute/path/cacti-mcp", "cacti-mcp"]
    }
  }
}
```

Configurez le client pour transmettre `CACTI_MCP_ENDPOINT` et `CACTI_MCP_TOKEN` au
sous-processus via son environnement ou son mécanisme de secrets. L'héritage de l'environnement
dépend du client. Il n'existe pas d'option de jeton en ligne de commande.

La distribution Python installable séparément fournit la commande console `cacti-mcp`.
Aucune publication sur PyPI n'est requise pour exécuter le dépôt local. Le plugin PHP n'a
aucune dépendance Python.

## Versions

La version de la distribution est enregistrée dans [pyproject.toml](../../../pyproject.toml).
En attendant que des versions taguées soient disponibles, utilisez une copie locale des sources ou
l'artefact `python-distributions` issu d'une
[exécution CI réussie](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
L'artefact contient un wheel et une archive source. Le paquet installé fournit
à la fois la commande `cacti-mcp` et `python -m cacti_mcp` ; il ne contient pas le
plugin PHP.

## Développement et tests

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Les tests couvrent la validation HTTP, l'isolation des identifiants, les requêtes bearer uniquement,
la pagination, l'expurgation des erreurs et un véritable échange en sous-processus client/serveur SDK avec
un serveur HTTP de fixture. Ils ne nécessitent pas d'installation Cacti active.

Le dépôt utilise `src/cacti_mcp/`, pytest, Ruff, uv et Hatchling. La CI teste
Python 3.12, 3.13 et 3.14. Une tâche de packaging distincte génère le wheel
et l'archive source, installe le wheel hors du dépôt et effectue un test rapide
des deux points d'entrée. Les distributions et les résultats de tests sont des artefacts de workflow.

## Contribution

Les pull requests sont dirigées vers `develop`. Gardez l'adaptateur compatible avec Python 3.12,
suivez la configuration Ruff existante et la structure de paquet `src/cacti_mcp/`, et
gardez stdout réservé aux messages MCP. Ajoutez des tests pour tout changement de comportement du transport ou des outils,
exécutez les vérifications ci-dessus et signez vos commits avec `git commit -s`.
Coordonnez les modifications d'API avec le plugin Cacti MCP et mettez à jour [docs/api.md](../../../docs/api.md).

## Licence

Copyright (C) 2026 Thomas Vincent. Publié sous licence GNU General Public
License, version 2 ou ultérieure. Voir [LICENSE](../../../LICENSE).
