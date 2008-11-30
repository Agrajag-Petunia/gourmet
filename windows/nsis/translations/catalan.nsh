;;

;;  catalan.nsh

;;

;;  Catalan language strings for the Windows Gourmet NSIS installer.

;;  Windows Code page: 1252

;;

;;  Author: "Bernat L�pez" <bernatl@adequa.net>

;;  Version 2

;;  



; Startup GTK+ check

!define GTK_INSTALLER_NEEDED			"L'entorn d'execuci� GTK+ no existeix o necessita �sser actualitzat.$\rSius plau instal.la la versi�${GTK_VERSION} o superior de l'entonr GTK+"



; License Page

!define GOURMET_LICENSE_BUTTON			"Seg�ent >"

!define GOURMET_LICENSE_BOTTOM_TEXT		"$(^Name) �s distribu�t sota llic�ncia GPLe. Podeu consultar la llic�ncia, nom�s per proposits informatius, aqu�. $_CLICK"



; Components Page

!define GOURMET_SECTION_TITLE			"Gourmet Recipe Manager (necessari)"

!define GTK_SECTION_TITLE			"Entorn d'Execuci� GTK+ (necessari)"

!define GTK_THEMES_SECTION_TITLE		"Temes GTK+"

!define GTK_NOTHEME_SECTION_TITLE		"Sense tema"

!define GTK_WIMP_SECTION_TITLE		"Tema Imwi"

!define GTK_BLUECURVE_SECTION_TITLE		"Tema Corba Blava"

!define GTK_LIGHTHOUSEBLUE_SECTION_TITLE	"Tema Light House Blue"

!define GOURMET_SECTION_DESCRIPTION		"Fitxers i dlls del nucli de Gourmet"

!define GTK_SECTION_DESCRIPTION		"Una eina IGU multiplataforma, utilitzada per Gourmet"

!define GTK_THEMES_SECTION_DESCRIPTION	"GTK+ Themes can change the look and feel of GTK+ applications."

!define GTK_NO_THEME_DESC			"No instal.lis un tema GTK+"

!define GTK_WIMP_THEME_DESC			"GTK-Imwi (imitador Windows) �s un tema GTK que s'integra perfectament en un entorn d'escriptori Windows."

!define GTK_BLUECURVE_THEME_DESC		"El tema Corba Blava."

!define GTK_LIGHTHOUSEBLUE_THEME_DESC	"The Lighthouseblue theme."



; GTK+ Directory Page

!define GTK_UPGRADE_PROMPT			"S'ha trobat una versi� antiga de l'entorn d'execuci� GTK. Vols actualitzar-la?$\rNota: Gourmet no funcionar� sino ho fas."



; Installer Finish Page

!define GOURMET_FINISH_VISIT_WEB_SITE		"Visita la p�gina web de Gourmet per Windows"



; Gourmet Section Prompts and Texts

!define GOURMET_UNINSTALL_DESC			"Gourmet (nom�s esborrar)"

!define GOURMET_PROMPT_WIPEOUT			"El teu directori antic de Gourmet ser� esborrat. Vols continuar?$\r$\rNota: Els plugins no est�ndards que tinguis instal.lats seran esborrats.$\rLes prefer�ncies d'usuari de Gourmet no es veruan afectades."

!define GOURMET_PROMPT_DIR_EXISTS		"El directori d'instal.laci� que has especificat ja existeix. Tots els continguts$\rseran esborrats. Vols continuar?"



; GTK+ Section Prompts

!define GTK_INSTALL_ERROR			"Error installlant l'entorn d'execuci� GTK+."

!define GTK_BAD_INSTALL_PATH			"El directori que has introdu�t no pot �sser accedit o creat."



; GTK+ Themes section

!define GTK_NO_THEME_INSTALL_RIGHTS		"No tens permisos per instal.lar un tema GTK+."



; Uninstall Section Prompts

!define un.GOURMET_UNINSTALL_ERROR_1		"L'instal.lador podria no trobar les entrades del registre de Gourmet.$\rProbablement un altre usuari ha instal.lat aquesta aplicaci�."

!define un.GOURMET_UNINSTALL_ERROR_2		"No tens perm�s per desinstal.lar aquesta aplicaci�."

