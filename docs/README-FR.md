<p align="center">
  <img src="../res/logo-header.svg" alt="VNFap - Your remote desktop"><br>
  <a href="#serveurs-publics-libres">Serveurs</a> -
  <a href="#étapes-brutes-de-la-compilationbuild">Build</a> -
  <a href="#comment-construire-avec-docker">Docker</a> -
  <a href="#structure-du-projet">Structure</a> -
  <a href="#images">Images</a><br>
  [<a href="../README.md">English</a>] | [<a href="README-UA.md">Українська</a>] | [<a href="README-CS.md">česky</a>] | [<a href="README-ZH.md">中文</a>] | [<a href="README-HU.md">Magyar</a>] | [<a href="README-ES.md">Español</a>] | [<a href="README-FA.md">فارسی</a>] | [<a href="README-DE.md">Deutsch</a>] | [<a href="README-PL.md">Polski</a>] | [<a href="README-ID.md">Indonesian</a>] | [<a href="README-FI.md">Suomi</a>] | [<a href="README-ML.md">മലയാളം</a>] | [<a href="README-JP.md">日本語</a>] | [<a href="README-NL.md">Nederlands</a>] | [<a href="README-IT.md">Italiano</a>] | [<a href="README-RU.md">Русский</a>] | [<a href="README-PTBR.md">Português (Brasil)</a>] | [<a href="README-EO.md">Esperanto</a>] | [<a href="README-KR.md">한국어</a>] | [<a href="README-AR.md">العربي</a>] | [<a href="README-VN.md">Tiếng Việt</a>] | [<a href="README-GR.md">Ελληνικά</a>]<br>
  <b>Nous avons besoin de votre aide pour traduire ce README dans votre langue maternelle</b>.
</p>



Encore un autre logiciel de bureau à distance, écrit en Rust. Fonctionne directement, aucune configuration n'est nécessaire. Vous avez le contrôle total de vos données, sans aucun souci de sécurité. Vous pouvez utiliser notre serveur de rendez-vous/relais, [configurer le vôtre](https://vnfap.com/server), ou [écrire votre propre serveur de rendez-vous/relais](https://github.com/gitxstudent/vnfap-server-demo).

VNFap accueille les contributions de tout le monde. Voir [`docs/CONTRIBUTING.md`](CONTRIBUTING.md) pour plus d'informations.

[**TÉLÉCHARGEMENT BINAIRE**](https://github.com/gitxstudent/vnfap/releases)

## Dépendances

Les versions de bureau utilisent [sciter](https://sciter.com/) pour l'interface graphique, veuillez télécharger la bibliothèque dynamique sciter vous-même.

[Windows](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.win/x64/sciter.dll) |
[Linux](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.lnx/x64/libsciter-gtk.so)
[macOS](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.osx/libsciter.dylib)

## Étapes brutes de la compilation/build

- Préparez votre environnement de développement Rust et votre environnement de compilation C++.

- Installez [vcpkg](https://github.com/microsoft/vcpkg), et définissez correctement la variable d'environnement `VCPKG_ROOT`.

  - Windows : vcpkg install libvpx:x64-windows-static libyuv:x64-windows-static opus:x64-windows-static aom:x64-windows-static
  - Linux/Osx : vcpkg install libvpx libyuv opus aom

- Exécuter `cargo run`

## Comment compiler/build sous Linux

### Ubuntu 18 (Debian 10)

```sh
sudo apt install -y g++ gcc git curl wget nasm yasm libgtk-3-dev clang libxcb-randr0-dev libxdo-dev libxfixes-dev libxcb-shape0-dev libxcb-xfixes0-dev libasound2-dev libpulse-dev cmake
```

### Fedora 28 (CentOS 8)

```sh
sudo yum -y install gcc-c++ git curl wget nasm yasm gcc gtk3-devel clang libxcb-devel libxdo-devel libXfixes-devel pulseaudio-libs-devel cmake alsa-lib-devel
```

### Arch (Manjaro)

```sh
sudo pacman -Syu --needed unzip git cmake gcc curl wget yasm nasm zip make pkg-config clang gtk3 xdotool libxcb libxfixes alsa-lib pipewire
```

### Installer vcpkg

```sh
git clone https://github.com/microsoft/vcpkg
cd vcpkg
git checkout 2023.04.15
cd ..
vcpkg/bootstrap-vcpkg.sh
export VCPKG_ROOT=$HOME/vcpkg
vcpkg/vcpkg install libvpx libyuv opus aom
```

### Corriger libvpx (Pour Fedora)

```sh
cd vcpkg/buildtrees/libvpx/src
cd *
./configure
sed -i 's/CFLAGS+=-I/CFLAGS+=-fPIC -I/g' Makefile
sed -i 's/CXXFLAGS+=-I/CXXFLAGS+=-fPIC -I/g' Makefile
make
cp libvpx.a $HOME/vcpkg/installed/x64-linux/lib/
cd
```

### Construire

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/gitxstudent/vnfap
cd vnfap
mkdir -p target/debug
wget https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.lnx/x64/libsciter-gtk.so
mv libsciter-gtk.so target/debug
Exécution du cargo
```

## Comment construire avec Docker

Commencez par cloner le dépôt et construire le conteneur Docker :

```sh
git clone https://github.com/gitxstudent/vnfap
cd vnfap
docker build -t "vnfap-builder" .
```

Ensuite, chaque fois que vous devez compiler le logiciel, exécutez la commande suivante :

```sh
docker run --rm -it -v $PWD:/home/user/vnfap -v vnfap-git-cache:/home/user/.cargo/git -v vnfap-registry-cache:/home/user/.cargo/registry -e PUID="$(id -u)" -e PGID="$(id -g)" vnfap-builder
```

Notez que la première compilation peut prendre plus de temps avant que les dépendances ne soient mises en cache, les compilations suivantes seront plus rapides. De plus, si vous devez spécifier différents arguments à la commande de compilation, vous pouvez le faire à la fin de la commande à la position `<OPTIONAL-ARGS>`. Par exemple, si vous voulez compiler une version de release optimisée, vous devez exécuter la commande ci-dessus suivie de `--release`. L'exécutable résultant sera disponible dans le dossier cible sur votre système, et peut être lancé avec :

```sh
target/debug/vnfap
```

Ou, si vous exécutez un exécutable provenant d'une release :

```sh
target/release/vnfap
```

Veuillez vous assurer que vous exécutez ces commandes à partir de la racine du dépôt VNFap, sinon l'application ne pourra pas trouver les ressources requises. Notez également que les autres sous-commandes de cargo telles que `install` ou `run` ne sont pas actuellement supportées par cette méthode car elles installeraient ou exécuteraient le programme à l'intérieur du conteneur au lieu de l'hôte.

## Structure du projet

- **[libs/hbb_common](https://github.com/gitxstudent/vnfap/tree/master/libs/hbb_common)** : codec vidéo, config, wrapper tcp/udp, protobuf, fonctions fs pour le transfert de fichiers, et quelques autres fonctions utilitaires.
- **[libs/scrap](https://github.com/gitxstudent/vnfap/tree/master/libs/scrap)** : capture d'écran
- **[libs/enigo](https://github.com/gitxstudent/vnfap/tree/master/libs/enigo)** : contrôle clavier/souris spécifique à la plate-forme
- **[src/ui](https://github.com/gitxstudent/vnfap/tree/master/src/ui)** : interface graphique
- **[src/server](https://github.com/gitxstudent/vnfap/tree/master/src/server)** : services audio/clipboard/input/vidéo, et connexions réseau
- **[src/client.rs](https://github.com/gitxstudent/vnfap/tree/master/src/client.rs)** : démarrer une connexion entre pairs
- **[src/rendezvous_mediator.rs](https://github.com/gitxstudent/vnfap/tree/master/src/rendezvous_mediator.rs)** : Communiquer avec [vnfap-server](https://github.com/gitxstudent/vnfap-server), attendre une connexion distante directe (TCP hole punching) ou relayée.
- **[src/platform](https://github.com/gitxstudent/vnfap/tree/master/src/platform)** : code spécifique à la plateforme

> [!Attention]
> **Avertissement contre l'utilisation abusive:** <br>
> Les développeurs de VNFap ne cautionnent ni ne soutiennent aucune utilisation non éthique ou illégale de ce logiciel. Toute utilisation abusive, telle que l'accès non autorisé, le contrôle ou l'invasion de la vie privée, est strictement contraire à nos directives. Les auteurs ne sont pas responsables de toute utilisation abusive de l'application.

## Images

![image](https://user-images.githubusercontent.com/71636191/113112362-ae4deb80-923b-11eb-957d-ff88daad4f06.png)

![image](https://user-images.githubusercontent.com/71636191/113112619-f705a480-923b-11eb-911d-97e984ef52b6.png)

![image](https://user-images.githubusercontent.com/71636191/113112857-3fbd5d80-923c-11eb-9836-768325faf906.png)

![image](https://user-images.githubusercontent.com/71636191/135385039-38fdbd72-379a-422d-b97f-33df71fb1cec.png)
