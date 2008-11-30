;;

;;  serbian-latin.nsh

;;

;;  Serbian (Latin) language strings for the Windows Gourmet NSIS installer.

;;  Windows Code page: 1250

;;

;;  Author: Danilo Segan <dsegan@gmx.net>

;;



; Startup GTK+ check

!define GTK_INSTALLER_NEEDED			"GTK+ okolina za izvr�avanje ili nije na�ena ili se moraunaprediti.$\rMolimo instalirajte v${GTK_VERSION} ili ve�u GTK+ okoline za izvr�avanje"



; Components Page

!define GOURMET_SECTION_TITLE			"Gourmet Recipe Manager (neophodno)"

!define GTK_SECTION_TITLE			"GTK+ okolina za izvr�avanje (neophodno)"

!define GTK_THEMES_SECTION_TITLE		"GTK+ teme"

!define GTK_NOTHEME_SECTION_TITLE		"Bez teme"

!define GTK_WIMP_SECTION_TITLE		"Wimp tema"

!define GTK_BLUECURVE_SECTION_TITLE		"Bluecurve tema"

!define GTK_LIGHTHOUSEBLUE_SECTION_TITLE	"Light House Blue tema"

!define GOURMET_SECTION_DESCRIPTION		"Osnovne Gourmet datoteke i dinami�ke biblioteke"

!define GTK_SECTION_DESCRIPTION		"Skup oru�a za grafi�ko okru�enje, za vi�e platformi, koristi ga Gourmet"

!define GTK_THEMES_SECTION_DESCRIPTION	"GTK+ teme menjaju izgled i na�in rada GTK+ aplikacija."

!define GTK_NO_THEME_DESC			"Ne instaliraj GTK+ temu"

!define GTK_WIMP_THEME_DESC			"GTK-Wimp (Windows imitator) je GTK tema koja se dobro uklapa u Windows radno okru�enje."

!define GTK_BLUECURVE_THEME_DESC		"Bluecurve tema."

!define GTK_LIGHTHOUSEBLUE_THEME_DESC	"Lighthouseblue tema."



; GTK+ Directory Page

!define GTK_UPGRADE_PROMPT			"Na�ena je stara verzija GTK+ izvr�ne okoline. Da li �elite da je unapredite?$\rPrimedba: Ukoliko to ne uradite, Gourmet mo�da ne�e raditi."



; Gourmet Section Prompts and Texts

!define GOURMET_UNINSTALL_DESC			"Gourmet (samo uklanjanje)"

!define GOURMET_PROMPT_WIPEOUT			"Va� stari Gourmet direktorijum �e biti obrisan. Da li �elite da nastavite?$\r$\rPrimedba: Svi nestandardni dodaci koje ste instalirali �e biti obrisani.$\rGourmet postavke korisnika ne�e biti promenjene."

!define GOURMET_PROMPT_DIR_EXISTS		"Instalacioni direktorijum koji ste naveli ve� postoji. Sav sadr�aj$\r�e biti obrisan. Da li �elite da nastavite?"



; GTK+ Section Prompts

!define GTK_INSTALL_ERROR			"Gre�ka prilikom instalacije GTK+ okoline za izvr�avanje."

!define GTK_BAD_INSTALL_PATH			"Putanja koju ste naveli se ne mo�e ni napraviti niti joj se mo�e pri�i."



; GTK+ Themes section

!define GTK_NO_THEME_INSTALL_RIGHTS		"Nemate ovla��enja za instalaciju GTK+ teme."



; Uninstall Section Prompts

!define un.GOURMET_UNINSTALL_ERROR_1         "Program za uklanjanje instalacije ne mo�e da prona�e stavke registra za Gourmet.$\rVerovatno je ovu aplikaciju instalirao drugi korisnik."

!define un.GOURMET_UNINSTALL_ERROR_2         "Nemate ovla��enja za deinstalaciju ove aplikacije."

