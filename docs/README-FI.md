<p align="center">
  <img src="../res/logo-header.svg" alt="VNFap - Etätyöpöytäsi"><br>
  <a href="#free-public-servers">Palvelimet</a> •
  <a href="#raw-steps-to-build">Rakenna</a> •
  <a href="#how-to-build-with-docker">Docker</a> •
  <a href="#file-structure">Rakenne</a> •
  <a href="#snapshot">Tilannevedos</a><br>
  [<a href="../README.md">English</a>] | [<a href="README-UA.md">Українська</a>] | [<a href="README-CS.md">česky</a>] | [<a href="README-ZH.md">中文</a>] | [<a href="README-HU.md">Magyar</a>] | [<a href="README-ES.md">Español</a>] | [<a href="README-FA.md">فارسی</a>] | [<a href="README-FR.md">Français</a>] | [<a href="README-DE.md">Deutsch</a>] | [<a href="README-PL.md">Polski</a>] | [<a href="README-ID.md">Indonesian</a>] | [<a href="README-ML.md">മലയാളം</a>] | [<a href="README-JP.md">日本語</a>] | [<a href="README-NL.md">Nederlands</a>] | [<a href="README-IT.md">Italiano</a>] | [<a href="README-RU.md">Русский</a>] | [<a href="README-PTBR.md">Português (Brasil)</a>] | [<a href="README-EO.md">Esperanto</a>] | [<a href="README-KR.md">한국어</a>] | [<a href="README-AR.md">العربي</a>] | [<a href="README-VN.md">Tiếng Việt</a>] | [<a href="README-GR.md">Ελληνικά</a>]<br>
  <b>Tarvitsemme apua tämän README-tiedoston kääntämiseksi äidinkielellesi</b>
</p>



Vielä yksi etätyöpöytäohjelmisto, ohjelmoitu Rust-kielellä. Toimii suoraan pakkauksesta, ei tarvitse asetusta. Hallitset täysin tietojasi, ei tarvitse murehtia turvallisuutta. Voit käyttää meidän rendezvous/relay-palvelinta, [aseta omasi](https://vnfap.com/server), tai [kirjoittaa oma rendezvous/relay-palvelin](https://github.com/gitxstudent/vnfap-server-demo).

VNFap toivottaa avustukset tervetulleiksi kaikilta. Katso lisätietoja [`docs/CONTRIBUTING.md`](CONTRIBUTING.md) avun saamiseksi.

[**BINAARILATAUS**](https://github.com/gitxstudent/vnfap/releases)

## Riippuvuudet

Desktop-versiot käyttävät [sciter](https://sciter.com/) graafisena käyttöliittymänä, lataa sciter-dynaaminen kirjasto itsellesi.

[Windows](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.win/x64/sciter.dll) |
[Linux](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.lnx/x64/libsciter-gtk.so) |
[MacOS](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.osx/libsciter.dylib)

## Rakentamisaskeleet harppoen

- Valmistele Rust-kehitysympäristö ja C++-rakentamisympäristö

- Asenna [vcpkg](https://github.com/microsoft/vcpkg), ja aseta `VCPKG_ROOT`-ympäristömuuttuja oikein

  - Windows: vcpkg install libvpx:x64-windows-static libyuv:x64-windows-static opus:x64-windows-static aom:x64-windows-static
  - Linux/MacOS: vcpkg install libvpx libyuv opus aom

- suorita `cargo run`

## Kuinka rakentaa Linux:issa

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

### Asenna vcpkg

```sh
git clone https://github.com/microsoft/vcpkg
cd vcpkg
git checkout 2023.04.15
cd ..
vcpkg/bootstrap-vcpkg.sh
export VCPKG_ROOT=$HOME/vcpkg
vcpkg/vcpkg install libvpx libyuv opus aom
```

### Korjaa libvpx (Fedora)

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

### Rakenna

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

## Kuinka rakennetaan Dockerin kanssa

Aloita kloonaamalla tietovarasto ja rakentamalla docker-säiliö:

```sh
git clone https://github.com/gitxstudent/vnfap
cd vnfap
docker build -t "vnfap-builder" .
```

Sitten, joka kerta kun sinun on rakennettava sovellus, suorita seuraava komento:

```sh
docker run --rm -it -v $PWD:/home/user/vnfap -v vnfap-git-cache:/home/user/.cargo/git -v vnfap-registry-cache:/home/user/.cargo/registry -e PUID="$(id -u)" -e PGID="$(id -g)" vnfap-builder
```

Huomaa, että ensimmäinen rakentaminen saattaa kestää pitempään ennen kuin riippuvuudet on siirretty välimuistiin, seuraavat rakentamiset ovat nopeampia. Lisäksi, jos sinun on määritettävä eri väittämiä rakentamiskomennolle, saatat tehdä sen niin, että komennon lopussa <OPTIONAL-ARGS>`-kohdassa. Esimerkiksi, jos haluat rakentaa optimoidun julkaisuversion, sinun on ajettava komento yllä siten, että sitä seuraa väittämä`--release`. Suoritettava tiedosto on saatavilla järjestelmäsi kohdehakemistossa, ja se voidaan suorittaa seuraavan kera:

```sh
target/debug/vnfap
```

Tai, jos olet suorittamassa jakeluversion suoritettavaa tiedostoa:

```sh
target/release/vnfap
```

Varmista, että suoritat näitä komentoja VNFaptop-tietovaraston juurihakemistossa, muutoin sovellus ei ehkä löydä vaadittuja resursseja. Huomaa myös, että muita cargo-alikomentoja kuten `install` tai `run` ei nykyisin tueta tässä menetelmässä, koska ne asentavat tai suorittavat ohjelman säiliön sisällä eikä isäntäohjelman sisällä.

## Tiedostorakenne

- **[libs/hbb_common](https://github.com/gitxstudent/vnfap/tree/master/libs/hbb_common)**: video codec, config, tcp/udp wrapper, protobuf, fs-funktiot tiedostosiirtoon, ja jotkut muut apuohjelmafunktiot
- **[libs/scrap](https://github.com/gitxstudent/vnfap/tree/master/libs/scrap)**: näyttökaappaukset
- **[libs/enigo](https://github.com/gitxstudent/vnfap/tree/master/libs/enigo)**: platform specific keyboard/mouse control
- **[src/ui](https://github.com/gitxstudent/vnfap/tree/master/src/ui)**: Graafinen käyttöliittymä
- **[src/server](https://github.com/gitxstudent/vnfap/tree/master/src/server)**: audio/clipboard/input/video services, and network connections
- **[src/client.rs](https://github.com/gitxstudent/vnfap/tree/master/src/client.rs)**: start a peer connection
- **[src/rendezvous_mediator.rs](https://github.com/gitxstudent/vnfap/tree/master/src/rendezvous_mediator.rs)**: Communicate with [vnfap-server](https://github.com/gitxstudent/vnfap-server), wait for remote direct (TCP hole punching) or relayed connection
- **[src/platform](https://github.com/gitxstudent/vnfap/tree/master/src/platform)**: platform specific code

## Tilannekuvat

![image](https://user-images.githubusercontent.com/71636191/113112362-ae4deb80-923b-11eb-957d-ff88daad4f06.png)

![image](https://user-images.githubusercontent.com/71636191/113112619-f705a480-923b-11eb-911d-97e984ef52b6.png)

![image](https://user-images.githubusercontent.com/71636191/113112857-3fbd5d80-923c-11eb-9836-768325faf906.png)

![image](https://user-images.githubusercontent.com/71636191/135385039-38fdbd72-379a-422d-b97f-33df71fb1cec.png)
