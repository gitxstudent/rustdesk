<p align="center">
  <img src="../res/logo-header.svg" alt="VNFap - Your remote desktop"><br>
  <a href="#ingyenes-publikus-szerverek">Szerverek</a> •
  <a href="#építési-pontok">Építés</a> •
  <a href="#hogyan-éptís-dockerrel">Docker</a> •
  <a href="#fájl-struktúra">Struktúra</a> •
  <a href="#képernyőképek">Képernyőképek</a><br>
  [<a href="../README.md">English</a>] | [<a href="README-UA.md">Українська</a>] | [<a href="README-CS.md">česky</a>] | [<a href="README-ZH.md">中文</a>] | [<a href="README-ES.md">Español</a>] | [<a href="README-FA.md">فارسی</a>] | [<a href="README-FR.md">Français</a>] | [<a href="README-DE.md">Deutsch</a>] | [<a href="README-PL.md">Polski</a>] | [<a href="README-ID.md">Indonesian</a>] | [<a href="README-FI.md">Suomi</a>] | [<a href="README-ML.md">മലയാളം</a>] | [<a href="README-JP.md">日本語</a>] | [<a href="README-NL.md">Nederlands</a>] | [<a href="README-IT.md">Italiano</a>] | [<a href="README-RU.md">Русский</a>] | [<a href="README-PTBR.md">Português (Brasil)</a>] | [<a href="README-EO.md">Esperanto</a>] | [<a href="README-KR.md">한국어</a>] | [<a href="README-AR.md">العربي</a>] | [<a href="README-VN.md">Tiếng Việt</a>] | [<a href="README-GR.md">Ελληνικά</a>]<br>
  <b>Kell a segítséged, hogy lefordítsuk ezt a README-t, <a href="https://github.com/gitxstudent/vnfap/tree/master/src/lang">a VNFap UI-t</a> és a <a href="https://github.com/vnfap/doc.vnfap.com">Dokumentációt</a> az anyanyelvedre</b>
</p>



A VNFap egy távoli elérésű asztali szoftver, Rust-ban írva. Működik mindenféle konfiguráció nélkül, feltelepítéssel, vagy anélkül. Az adataidat teljesen te kezeled, nincs szükség aggódásra a harmadik felek miatt. Használhatod a VNFap punblikus randevú/relay szervereit, [hostolhatsz sajátot](https://vnfap.com/server), vagy akár [írhatsz is egyet](https://github.com/gitxstudent/vnfap-server-demo).

![image](https://user-images.githubusercontent.com/71636191/171661982-430285f0-2e12-4b1d-9957-4a58e375304d.png)

A VNFap szívesen fogad minden contributiont, támogatást mindenkitől. Lásd a [`docs/CONTRIBUTING.md`](CONTRIBUTING.md) fájlt a kezdéshez.

[**Hogyan működik a VNFap?**](https://github.com/gitxstudent/vnfap/wiki/How-does-VNFap-work%3F)

[**BINARY LELTÖLTÉS**](https://github.com/gitxstudent/vnfap/releases)

[<img src="https://fdroid.gitlab.io/artwork/badge/get-it-on.png"
    alt="Get it on F-Droid"
    height="80">](https://f-droid.org/en/packages/com.carriez.flutter_hbb)

## Dependencies

Az asztali verziók [sciter](https://sciter.com/)-t használnak a GUI-hoz, kérlek telepítsd a dynamikus könyvtárat magad.

[Windows](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.win/x64/sciter.dll) |
[Linux](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.lnx/x64/libsciter-gtk.so) |
[MacOS](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.osx/libsciter.dylib)

A telefonos verziók Flutter-t hasznának. Később lehetséges hogy Sciterről Flutterre migrálunk az asztali verziókban is.

## Építési pontok

- Készítsd elő a Rust, C++ fejlesztői környezetet (env)

- Telepítsd a [vcpkg](https://github.com/microsoft/vcpkg)-t, és állítsd be a `VCPKG_ROOT` környezeti változót helyesen

  - Windows: vcpkg install libvpx:x64-windows-static libyuv:x64-windows-static opus:x64-windows-static aom:x64-windows-static
  - Linux/MacOS: vcpkg install libvpx libyuv opus aom

- Futtasd a `cargo run` parancsot

## [Építés](https://vnfap.com/docs/hu/dev/build/)

## Hogyan építs Linuxon

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

### Telepítsd a vcpkg-t

```sh
git clone https://github.com/microsoft/vcpkg
cd vcpkg
git checkout 2023.04.15
cd ..
vcpkg/bootstrap-vcpkg.sh
export VCPKG_ROOT=$HOME/vcpkg
vcpkg/vcpkg install libvpx libyuv opus aom
```

### Fixeld a libvpx-t (Fedora-n csak)

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

### Építés

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/gitxstudent/vnfap
cd vnfap
mkdir -p target/debug
wget https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.lnx/x64/libsciter-gtk.so
mv libsciter-gtk.so target/debug
VCPKG_ROOT=$HOME/vcpkg cargo run
```

## Hogyan építs Dockerrel

Kezdjünk a repo clónozásával, majd pedig a Docker container megépítésével:

```sh
git clone https://github.com/gitxstudent/vnfap
cd vnfap
docker build -t "vnfap-builder" .
```

Ezután, minden egyes alkalommal amikor meg kell építened a VNFap-et, futtasd a kövezkező parancsot:

```sh
docker run --rm -it -v $PWD:/home/user/vnfap -v vnfap-git-cache:/home/user/.cargo/git -v vnfap-registry-cache:/home/user/.cargo/registry -e PUID="$(id -u)" -e PGID="$(id -g)" vnfap-builder
```

Fontos, hogy az első építés lehet hogy több ideig fog tartani mint a következőek, mivel a dependenciek még nincsenek cachelve. Emelett, ha esetleg szeretnél valamilyen argumentumot hozzáadni az építő parancshoz, akkor megteheted a paracssor végén, a `<OPTIONAL-ARGS>` argumentum használatával. Például ha egy optimalizált release éptést szeretnél megépíteni, akkor add hozzá a fenti parancsorhoz a `--release` opciót. A futtatható binary elérhető lesz a target mappában a rendszereden, futtatni a következőképpen tudod: 

```sh
target/debug/vnfap
```

Vagy ha release binary, akkor:

```sh
target/release/vnfap
```

Kérlek mindenképpen nézd meg hogy ezeket a parancsokat a root VNFap mappában futtatod e, különben a VNFap lehet hogy nem fogja megtalálni az építéshez szükséges elemeket. Fontos az is, hogy jelenleg más cargo subparancsok, például `install`vagy `run` nem támogatottak, mivel egy Dockeres építés esetén elindítanák a programot a containeren belül.


## Fájl Struktúra

- **[libs/hbb_common](https://github.com/gitxstudent/vnfap/tree/master/libs/hbb_common)**: video codec, config, tcp/udp wrapper, protobuf, fs functions for file transfer, and some other utility functions
- **[libs/scrap](https://github.com/gitxstudent/vnfap/tree/master/libs/scrap)**: screen capture
- **[libs/enigo](https://github.com/gitxstudent/vnfap/tree/master/libs/enigo)**: platform specific keyboard/mouse control
- **[src/ui](https://github.com/gitxstudent/vnfap/tree/master/src/ui)**: GUI
- **[src/server](https://github.com/gitxstudent/vnfap/tree/master/src/server)**: audio/clipboard/input/video services, and network connections
- **[src/client.rs](https://github.com/gitxstudent/vnfap/tree/master/src/client.rs)**: start a peer connection
- **[src/rendezvous_mediator.rs](https://github.com/gitxstudent/vnfap/tree/master/src/rendezvous_mediator.rs)**: Communicate with [vnfap-server](https://github.com/gitxstudent/vnfap-server), wait for remote direct (TCP hole punching) or relayed connection
- **[src/platform](https://github.com/gitxstudent/vnfap/tree/master/src/platform)**: platform specific code
- **[flutter](https://github.com/gitxstudent/vnfap/tree/master/flutter)**: Flutter code for mobile
- **[flutter/web/js](https://github.com/gitxstudent/vnfap/tree/master/flutter/web/js)**: Javascript for Flutter web client

## Képernyőképek

![image](https://user-images.githubusercontent.com/71636191/113112362-ae4deb80-923b-11eb-957d-ff88daad4f06.png)

![image](https://user-images.githubusercontent.com/71636191/113112619-f705a480-923b-11eb-911d-97e984ef52b6.png)

![image](https://user-images.githubusercontent.com/71636191/113112857-3fbd5d80-923c-11eb-9836-768325faf906.png)

![image](https://user-images.githubusercontent.com/71636191/135385039-38fdbd72-379a-422d-b97f-33df71fb1cec.png)
