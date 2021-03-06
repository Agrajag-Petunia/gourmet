;;

;;  polish.nsh

;;

;;  Polish language strings for the Windows Gourmet NSIS installer.

;;  Windows Code page: 1250

;;

;;  Author: Jan Eldenmalm <jan.eldenmalm@amazingports.com>

;;  Version 2

;;



; Startup GTK+ check

!define GTK_INSTALLER_NEEDED			"Runtime �rodowiska GTK+ zosta� zagubiony lub wymaga upgrade-u.$\r Prosz� zainstaluj v${GTK_VERSION} albo wy�sz� wersj� runtime-u GTK+."



; License Page

!define GOURMET_LICENSE_BUTTON			"Dalej >"

!define GOURMET_LICENSE_BOTTOM_TEXT		"$(^Name) jest wydzielone w licencji GPL. Udziela si� licencji wy��cznie do cel�w informacyjnych. $_CLICK"



; Components Page

!define GOURMET_SECTION_TITLE			"Wymagany jest Gourmet Recipe Manager"

!define GTK_SECTION_TITLE			"Wymagany jest runtime �rodowiska GTK+"

!define GTK_THEMES_SECTION_TITLE		"Temat GTK+"

!define GTK_NOTHEME_SECTION_TITLE		"Brak temat�w"

!define GTK_WIMP_SECTION_TITLE		"Temat Wimp"

!define GTK_BLUECURVE_SECTION_TITLE		"Temat Bluecurve "

!define GTK_LIGHTHOUSEBLUE_SECTION_TITLE	"Temat Light House Blue"

!define GOURMET_SECTION_DESCRIPTION		"Zbiory Core Gourmet oraz dll"

!define GTK_SECTION_DESCRIPTION		"Wieloplatformowe narz�dzie GUI, u�ywane w Gourmet"

!define GTK_THEMES_SECTION_DESCRIPTION	"Tematy GTK+ mog� zmieni� wygl�d i dzia�anie aplikacji GTK+ ."

!define GTK_NO_THEME_DESC			"Nie instaluj temat�w GTK+"

!define GTK_WIMP_THEME_DESC			"GTK-Wimp (Windows impersonator) to temat GTK kt�ry doskonale wkomponowuje si� w �rodowisko systemu Windows."

!define GTK_BLUECURVE_THEME_DESC		"Temat The Bluecurve."

!define GTK_LIGHTHOUSEBLUE_THEME_DESC	"Temat Lighthouseblue."



; GTK+ Directory Page

!define GTK_UPGRADE_PROMPT			"Znaleziono star� wersj� runtime-u GTK+. Czy chcesz upgrade-owa�?$\rNote: Gourmet mo�e nie dzia�a� je�li nie wykonasz procedury."



; Installer Finish Page

!define GOURMET_FINISH_VISIT_WEB_SITE		"Wejd� na stron� Gourmet Web Page"



; Gourmet Section Prompts and Texts

!define GOURMET_UNINSTALL_DESC			"Gourmet (usu� program)"

!define GOURMET_PROMPT_WIPEOUT			"Stary katalog Gourmet zosta� usuni�ty. Czy chcesz kontunuowa�?$\r$\rNote: Wszystkie stare - niestandardowe plugin-y zosta�y usuni�te.$\r Ustawienia u�utkownika Gourmet b�d� wy��czone."

!define GOURMET_PROMPT_DIR_EXISTS		"Wybrany katalog instalacyjny ju� istnieje. Jego zawarto�� $\r zostanie skasowana. Czy chcesz kontunuowa�?"



; GTK+ Section Prompts

!define GTK_INSTALL_ERROR			"B��d instalacji runtime-a GTK+."

!define GTK_BAD_INSTALL_PATH			"Nie ma dost�pu do wybranej �cie�ki / �aty."



; GTK+ Themes section

!define GTK_NO_THEME_INSTALL_RIGHTS		"Nie masz uprawnie� do zainstalowania tematu GTK+."



; Uninstall Section Prompts

!define un.GOURMET_UNINSTALL_ERROR_1		"Deinstalator nie mo�e znale�� rejestr�w dla Gourmet.$\r Wskazuje to na to, �e instalacj� przeprowadzi� inny u�ytkownik."

!define un.GOURMET_UNINSTALL_ERROR_2		"Nie masz uprawnie� do deinstalacji tej aplikacji."

