Name:       vnfap
Version:    1.4.0
Release:    0
Summary:    RPM package
License:    GPL-3.0
URL:        https://vnfap.com
Vendor:     vnfap <info@vnfap.com>
Requires:   gtk3 libxcb libxdo libXfixes alsa-lib libva2 pam gstreamer1-plugins-base
Recommends: libayatana-appindicator-gtk3

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/

%description
The best open-source remote desktop client software, written in Rust.

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

%global __python %{__python3}

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/vnfap/
mkdir -p %{buildroot}/usr/share/vnfap/files/
mkdir -p %{buildroot}/usr/share/icons/hicolor/256x256/apps/
mkdir -p %{buildroot}/usr/share/icons/hicolor/scalable/apps/
install -m 755 $HBB/target/release/vnfap %{buildroot}/usr/bin/vnfap
install $HBB/libsciter-gtk.so %{buildroot}/usr/share/vnfap/libsciter-gtk.so
install $HBB/res/vnfap.service %{buildroot}/usr/share/vnfap/files/
install $HBB/res/128x128@2x.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/vnfap.png
install $HBB/res/scalable.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/vnfap.svg
install $HBB/res/vnfap.desktop %{buildroot}/usr/share/vnfap/files/
install $HBB/res/vnfap-link.desktop %{buildroot}/usr/share/vnfap/files/

%files
/usr/bin/vnfap
/usr/share/vnfap/libsciter-gtk.so
/usr/share/vnfap/files/vnfap.service
/usr/share/icons/hicolor/256x256/apps/vnfap.png
/usr/share/icons/hicolor/scalable/apps/vnfap.svg
/usr/share/vnfap/files/vnfap.desktop
/usr/share/vnfap/files/vnfap-link.desktop
/usr/share/vnfap/files/__pycache__/*

%changelog
# let's skip this for now

%pre
# can do something for centos7
case "$1" in
  1)
    # for install
  ;;
  2)
    # for upgrade
    systemctl stop vnfap || true
  ;;
esac

%post
cp /usr/share/vnfap/files/vnfap.service /etc/systemd/system/vnfap.service
cp /usr/share/vnfap/files/vnfap.desktop /usr/share/applications/
cp /usr/share/vnfap/files/vnfap-link.desktop /usr/share/applications/
systemctl daemon-reload
systemctl enable vnfap
systemctl start vnfap
update-desktop-database

%preun
case "$1" in
  0)
    # for uninstall
    systemctl stop vnfap || true
    systemctl disable vnfap || true
    rm /etc/systemd/system/vnfap.service || true
  ;;
  1)
    # for upgrade
  ;;
esac

%postun
case "$1" in
  0)
    # for uninstall
    rm /usr/share/applications/vnfap.desktop || true
    rm /usr/share/applications/vnfap-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
  ;;
esac
