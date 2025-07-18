<p align="center">
  <img src="../res/logo-header.svg" alt="VNFap - Your remote desktop"><br>
  <a href="#free-public-servers">Servers</a> •
  <a href="#raw-steps-to-build">Build</a> •
  <a href="#how-to-build-with-docker">Docker</a> •
  <a href="#file-structure">Structure</a> •
  <a href="#snapshot">Snapshot</a><br>
  [<a href="../README.md">English</a>] | [<a href="README-UA.md">Українська</a>] | [<a href="README-CS.md">česky</a>] | [<a href="README-ZH.md">中文</a>] | [<a href="README-HU.md">Magyar</a>] | [<a href="README-ES.md">Español</a>] | [<a href="README-FA.md">فارسی</a>] | [<a href="README-FR.md">Français</a>] | [<a href="README-DE.md">Deutsch</a>] | [<a href="README-PL.md">Polski</a>] | [<a href="README-FI.md">Suomi</a>] | [<a href="README-ML.md">മലയാളം</a>] | [<a href="README-JP.md">日本語</a>] | [<a href="README-NL.md">Nederlands</a>] | [<a href="README-IT.md">Italiano</a>] | [<a href="README-RU.md">Русский</a>] | [<a href="README-PTBR.md">Português (Brasil)</a>] | [<a href="README-EO.md">Esperanto</a>] | [<a href="README-KR.md">한국어</a>] | [<a href="README-AR.md">العربي</a>] | [<a href="README-VN.md">Tiếng Việt</a>] | [<a href="README-GR.md">Ελληνικά</a>]<br>
  <b>Kami membutuhkan bantuanmu untuk menterjemahkan file README dan <a href="https://github.com/gitxstudent/vnfap/tree/master/src/lang">VNFap UI</a> ke Bahasa Indonesia</b>
</p>



[![Open Bounties](https://img.shields.io/endpoint?url=https%3A%2F%2Fconsole.algora.io%2Fapi%2Fshields%2Fvnfap%2Fbounties%3Fstatus%3Dopen)](https://console.algora.io/org/vnfap/bounties?status=open)

Merupakan perangkat lunak Remote Desktop yang baru, dan dibangun dengan Rust. Bahkan kamu bisa langsung menggunakannya tanpa perlu melakukan konfigurasi tambahan. Serta memiliki kontrol penuh terhadap semua data, tanpa perlu merasa was-was tentang isu keamanan, dan yang lebih menarik adalah memiliki opsi untuk menggunakan server rendezvous/relay milik kami, [konfigurasi server sendiri](https://vnfap.com/server), atau [tulis rendezvous/relay server anda sendiri](https://github.com/gitxstudent/vnfap-server-demo).

![image](https://user-images.githubusercontent.com/71636191/171661982-430285f0-2e12-4b1d-9957-4a58e375304d.png)

VNFap mengajak semua orang untuk ikut berkontribusi. Lihat [`docs/CONTRIBUTING-ID.md`](CONTRIBUTING-ID.md) untuk melihat panduan.

[**FAQ**](https://github.com/gitxstudent/vnfap/wiki/FAQ)

[**UNDUH BINARY**](https://github.com/gitxstudent/vnfap/releases)

[**NIGHTLY BUILD**](https://github.com/gitxstudent/vnfap/releases/tag/nightly)

[<img src="https://fdroid.gitlab.io/artwork/badge/get-it-on.png"
    alt="Get it on F-Droid"
    height="80">](https://f-droid.org/en/packages/com.carriez.flutter_hbb)

## Dependensi

Pada versi desktop, antarmuka pengguna (GUI) menggunakan [Sciter](https://sciter.com/) atau flutter

Kamu bisa mengunduh Sciter dynamic library disini.

[Windows](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.win/x64/sciter.dll) |
[Linux](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.lnx/x64/libsciter-gtk.so) |
[MacOS](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.osx/libsciter.dylib)

## Langkah awal untuk memulai

- Siapkan env development Rust dan env build C++

- Install [vcpkg](https://github.com/microsoft/vcpkg), dan atur variabel env `VCPKG_ROOT` dengan benar

  - Windows: vcpkg install libvpx:x64-windows-static libyuv:x64-windows-static opus:x64-windows-static aom:x64-windows-static
  - Linux/MacOS: vcpkg install libvpx libyuv opus aom

- jalankan `cargo run`

## [Build](https://vnfap.com/docs/en/dev/build/)

## Cara Build di Linux

### Ubuntu 18 (Debian 10)

```sh
sudo apt install -y zip g++ gcc git curl wget nasm yasm libgtk-3-dev clang libxcb-randr0-dev libxdo-dev \
        libxfixes-dev libxcb-shape0-dev libxcb-xfixes0-dev libasound2-dev libpulse-dev cmake make \
        libclang-dev ninja-build libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
```

### Fedora 28 (CentOS 8)

```sh
sudo yum -y install gcc-c++ git curl wget nasm yasm gcc gtk3-devel clang libxcb-devel libxdo-devel libXfixes-devel pulseaudio-libs-devel cmake alsa-lib-devel
```

### Arch (Manjaro)

```sh
sudo pacman -Syu --needed unzip git cmake gcc curl wget yasm nasm zip make pkg-config clang gtk3 xdotool libxcb libxfixes alsa-lib pipewire
```

### Install vcpkg

```sh
git clone https://github.com/microsoft/vcpkg
cd vcpkg
git checkout 2023.04.15
cd ..
vcpkg/bootstrap-vcpkg.sh
export VCPKG_ROOT=$HOME/vcpkg
vcpkg/vcpkg install libvpx libyuv opus aom
```

### Mengatasi masalah libvpx (Untuk Fedora)

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

### Build

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

## Cara Build dengan Docker

Mulailah dengan melakukan kloning (clone) repositori dan build dengan docker container:

```sh
git clone https://github.com/gitxstudent/vnfap
cd vnfap
docker build -t "vnfap-builder" .
```

Selanjutnya, setiap kali ketika kamu akan melakukan build aplikasi, jalankan perintah berikut:

```sh
docker run --rm -it -v $PWD:/home/user/vnfap -v vnfap-git-cache:/home/user/.cargo/git -v vnfap-registry-cache:/home/user/.cargo/registry -e PUID="$(id -u)" -e PGID="$(id -g)" vnfap-builder
```

Perlu diingat bahwa pada saat build pertama kali, mungkin memerlukan waktu lebih lama sebelum dependensi di-cache, build berikutnya akan lebih cepat. Selain itu, jika perlu menentukan argumen yang berbeda untuk perintah build, kamu dapat melakukannya di akhir perintah di posisi `<OPTIONAL-ARGS>`. Misalnya, jika ingin membangun versi rilis yang dioptimalkan, jalankan perintah di atas dan tambahkan `--release`. Hasil eksekusi perintah tersebut akan tersimpan pada target folder di sistem kamu, dan dapat dijalankan dengan:

```sh
target/debug/vnfap
```

Atau, jika kamu menjalankan rilis yang dapat dieksekusi:

```sh
target/release/vnfap
```

Harap pastikan bahwa kamu menjalankan perintah ini dari repositori root VNFap, jika tidak demikian, aplikasi mungkin tidak dapat menemukan sumber yang diperlukan. Dan juga, perintah cargo seperti `install` atau `run` saat ini tidak didukung melalui metode ini karena, proses menginstal atau menjalankan program terjadi di dalam container bukan pada host.

## Struktur File

- **[libs/hbb_common](https://github.com/gitxstudent/vnfap/tree/master/libs/hbb_common)**: video codec, config, tcp/udp wrapper, protobuf, fs functions untuk transfer file, dan beberapa fungsi utilitas lainnya
- **[libs/scrap](https://github.com/gitxstudent/vnfap/tree/master/libs/scrap)**: screen capture
- **[libs/enigo](https://github.com/gitxstudent/vnfap/tree/master/libs/enigo)**: spesifikasi platform keyboard/mouse control
- **[src/ui](https://github.com/gitxstudent/vnfap/tree/master/src/ui)**: GUI
- **[src/server](https://github.com/gitxstudent/vnfap/tree/master/src/server)**: audio/clipboard/input/video services, dan network connections
- **[src/client.rs](https://github.com/gitxstudent/vnfap/tree/master/src/client.rs)**: start a peer connection
- **[src/rendezvous_mediator.rs](https://github.com/gitxstudent/vnfap/tree/master/src/rendezvous_mediator.rs)**: Komunikasi dengan [vnfap-server](https://github.com/gitxstudent/vnfap-server), menunggu untuk remote direct (TCP hole punching) atau relayed connection
- **[src/platform](https://github.com/gitxstudent/vnfap/tree/master/src/platform)**: kode khusus platform

## Snapshots

![image](https://user-images.githubusercontent.com/71636191/113112362-ae4deb80-923b-11eb-957d-ff88daad4f06.png)

![image](https://user-images.githubusercontent.com/71636191/113112619-f705a480-923b-11eb-911d-97e984ef52b6.png)

![image](https://user-images.githubusercontent.com/71636191/113112857-3fbd5d80-923c-11eb-9836-768325faf906.png)

![image](https://user-images.githubusercontent.com/71636191/135385039-38fdbd72-379a-422d-b97f-33df71fb1cec.png)
