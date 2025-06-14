<p align="center">
  <img src="../res/logo-header.svg" alt="VNFap – vaše vzdálená plocha"><br>
  <a href="#free-public-servers">Servery</a> •
  <a href="#raw-steps-to-build">Sestavení ze zdrojových kódů</a> •
  <a href="#how-to-build-with-docker">Docker</a> •
  <a href="#file-structure">Struktura</a> •
  <a href="#snapshot">Ukázky</a><br>
  [<a href="../README.md">English</a>] | [<a href="README-UA.md">Українська</a>] | [<a href="README-ZH.md">中文</a>] | [<a href="README-HU.md">Magyar</a>] | [<a href="README-ES.md">Español</a>] | [<a href="README-FA.md">فارسی</a>] | [<a href="README-FR.md">Français</a>] | [<a href="README-DE.md">Deutsch</a>] | [<a href="README-PL.md">Polski</a>] | [<a href="README-ID.md">Indonesian</a>] | [<a href="README-FI.md">Suomi</a>] | [<a href="README-ML.md">മലയാളം</a>] | [<a href="README-JP.md">日本語</a>] | [<a href="README-NL.md">Nederlands</a>] | [<a href="README-IT.md">Italiano</a>] | [<a href="README-RU.md">Русский</a>] | [<a href="README-PTBR.md">Português (Brasil)</a>] | [<a href="README-EO.md">Esperanto</a>] | [<a href="README-KR.md">한국어</a>] | [<a href="README-AR.md">العربي</a>] | [<a href="README-VN.md">Tiếng Việt</a>] | [<a href="README-GR.md">Ελληνικά</a>]<br>
  <b>Potřebujeme Vaši pomoc s překladem tohoto README, <a href="https://github.com/gitxstudent/vnfap/tree/master/src/lang">uživatelského rozhraní aplikace VNFap</a> a <a href="https://github.com/vnfap/doc.vnfap.com">dokumentace k ní</a> do vašeho jazyka</b>
</p>




Zase další software pro přístup k ploše na dálku, naprogramovaný v jazyce Rust. Funguje hned tak, jak je – není třeba žádného nastavování. Svá data máte ve svých rukách, bez obav o zabezpečení. Je možné používat námi poskytovaný propojovací/předávací (relay) server, [vytvořit si svůj vlastní](https://vnfap.com/server), nebo [si dokonce svůj vlastní naprogramovat](https://github.com/gitxstudent/vnfap-server-demo), budete-li chtít.

Projekt VNFap vítá přiložení ruky k dílu od každého. Jak začít se dozvíte z [`docs/CONTRIBUTING.md`](CONTRIBUTING.md).

[**Jak VNFap funguje?**](https://github.com/gitxstudent/vnfap/wiki/How-does-VNFap-work%3F)

[**STAHOVÁNÍ ZKOMPILOVANÝCH APLIKACÍ**](https://github.com/gitxstudent/vnfap/releases)

## Softwarové součásti, na kterých závisí

Varianta pro počítač používá pro grafické uživatelské rozhraní [sciter](https://sciter.com/) – stáhněte si potřebnou knihovnu.

[Windows](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.win/x64/sciter.dll) |
[Linux](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.lnx/x64/libsciter-gtk.so) |
[MacOS](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.osx/libsciter.dylib)

Varianta pro mobilní platformy používá aplikační rámec (framework) Flutter. Na tu také v budoucnu předěláme i variantu pro počítač.

## Stručně kroky pro sestavení ze zdrojových kódů

- Připravte si vývojové prostředí pro jazyky Rust a C++

- Nainstalujte [vcpkg](https://github.com/microsoft/vcpkg), a správně nastavte proměnnou prostředí `VCPKG_ROOT`

  - Windows: vcpkg install libvpx:x64-windows-static libyuv:x64-windows-static opus:x64-windows-static aom:x64-windows-static
  - Linux/MacOS: vcpkg install libvpx libyuv opus aom

- spusťte `cargo run`

## [Sestavení ze zdrojových kódů](https://vnfap.com/docs/en/dev/build/)

## Jak zkompilovat na Linuxu

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

### Instalace vcpkg

```sh
git clone https://github.com/microsoft/vcpkg
cd vcpkg
git checkout 2023.04.15
cd ..
vcpkg/bootstrap-vcpkg.sh
export VCPKG_ROOT=$HOME/vcpkg
vcpkg/vcpkg install libvpx libyuv opus aom
```

### Oprava libvpx (pro Fedoru)

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

### Sestavení

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

## Jak sestavit prostřednictvím Docker kontejnerizace

Začněte tím, že si naklonujete tento repozitář a sestavíte docker kontejner:

```sh
git clone https://github.com/gitxstudent/vnfap
cd vnfap
docker build -t "vnfap-builder" .
```

Poté pokaždé, když bude třeba aplikaci sestavit, spusťte následující příkaz:

```sh
docker run --rm -it -v $PWD:/home/user/vnfap -v vnfap-git-cache:/home/user/.cargo/git -v vnfap-registry-cache:/home/user/.cargo/registry -e PUID="$(id -u)" -e PGID="$(id -g)" vnfap-builder
```

Všimněte si, že prvotní sestavení může trvat déle (než se do mezipaměti uloží veškeré softwarové součásti, které jsou potřeba) – následná opakování už budou rychlejší. Pokud navíc potřebujete zadat různé argumenty příkazu pro sestavení, můžete tak učinit na konci příkazu v pozici `<OPTIONAL-ARGS>`. Například, pokud byste chtěli sestavit optimalizovanou verzi pro vydání, spustili byste výše uvedený příkaz následovaný `--release`. Výsledný spustitelný soubor se objeví v cílové složce na vašem systému a bude ho možné spustit pomocí:

```sh
target/debug/vnfap
```

Nebo, pokud spouštíte variantu pro vydání:

```sh
target/release/vnfap
```

Ujistěte se, že tyto příkazy spouštíte z kořenového adresáře VNFap, jinak aplikace nemusí být schopná nalézt potřebné prostředky (resources). Také si všimněte, že ostatní dílčí príkazy nástroje cargo, jako třeba `install` nebo `run` zatím nejsou prostřednictvím této metody podporovány, protože by vedly k instalaci či spuštění program uvnitř kontejneru namísto přímo v systému.

## Struktura souborů

- **[libs/hbb_common](https://github.com/gitxstudent/vnfap/tree/master/libs/hbb_common)**: kodek videa, nastavení, obalovaní tcp/udp, vyrovnávací paměť protokolu, funkce souborového systému pro přenos souborů a pár dalších podpůrných funkcí
- **[libs/scrap](https://github.com/gitxstudent/vnfap/tree/master/libs/scrap)**: zachytávání obsahu obrazovky
- **[libs/enigo](https://github.com/gitxstudent/vnfap/tree/master/libs/enigo)**: ovládání klávesnice/myši pro jednotlivé platformy
- **[src/ui](https://github.com/gitxstudent/vnfap/tree/master/src/ui)**: grafické uživatelské rozhraní
- **[src/server](https://github.com/gitxstudent/vnfap/tree/master/src/server)**: služby pro zvuk/schránku/zadávání/video a síťová spojení
- **[src/client.rs](https://github.com/gitxstudent/vnfap/tree/master/src/client.rs)**: spouští připojení k protějšku
- **[src/rendezvous_mediator.rs](https://github.com/gitxstudent/vnfap/tree/master/src/rendezvous_mediator.rs)**: komunikace s [vnfap-server](https://github.com/gitxstudent/vnfap-server), očekávání vzdálených příméhých („proděrováváním“ TCP) nebo předávaných (relay) spojení
- **[src/platform](https://github.com/gitxstudent/vnfap/tree/master/src/platform)**: zdrojové kódy, specifické pro jednotlivé platformy
- **[flutter](https://github.com/gitxstudent/vnfap/tree/master/flutter)**: zdrojové kódy pro použití s aplikačním rámcem (framework) Flutter pro mobilní platformy
- **[flutter/web/js](https://github.com/gitxstudent/vnfap/tree/master/flutter/web/js)**: Javascript pro Flutter webový klient

## Ukázky

![image](https://user-images.githubusercontent.com/71636191/113112362-ae4deb80-923b-11eb-957d-ff88daad4f06.png)

![image](https://user-images.githubusercontent.com/71636191/113112619-f705a480-923b-11eb-911d-97e984ef52b6.png)

![image](https://user-images.githubusercontent.com/71636191/113112857-3fbd5d80-923c-11eb-9836-768325faf906.png)

![image](https://user-images.githubusercontent.com/71636191/135385039-38fdbd72-379a-422d-b97f-33df71fb1cec.png)
