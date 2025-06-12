Name:       vnfap
Version:    1.4.0
Release:    0
Summary:    RPM package
License:    GPL-3.0
URL:        https://vnfap.com
Vendor:     vnfap <info@vnfap.com>
Requires:   gtk3 libxcb libxdo libXfixes alsa-lib libva pam gstreamer1-plugins-base
Recommends: libayatana-appindicator-gtk3
Provides:   libdesktop_drop_plugin.so()(64bit), libdesktop_multi_window_plugin.so()(64bit), libfile_selector_linux_plugin.so()(64bit), libflutter_custom_cursor_plugin.so()(64bit), libflutter_linux_gtk.so()(64bit), libscreen_retriever_plugin.so()(64bit), libtray_manager_plugin.so()(64bit), liburl_launcher_linux_plugin.so()(64bit), libwindow_manager_plugin.so()(64bit), libwindow_size_plugin.so()(64bit), libtexture_rgba_renderer_plugin.so()(64bit)

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/

%description
The best open-source remote desktop client software, written in Rust.

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

# %global __python %{__python3}

%install

mkdir -p "%{buildroot}/usr/share/vnfap" && cp -r ${HBB}/flutter/build/linux/x64/release/bundle/* -t "%{buildroot}/usr/share/vnfap"
mkdir -p "%{buildroot}/usr/bin"
install -Dm 644 $HBB/res/vnfap.service -t "%{buildroot}/usr/share/vnfap/files"
install -Dm 644 $HBB/res/vnfap.desktop -t "%{buildroot}/usr/share/vnfap/files"
install -Dm 644 $HBB/res/vnfap-link.desktop -t "%{buildroot}/usr/share/vnfap/files"
install -Dm 644 $HBB/res/128x128@2x.png "%{buildroot}/usr/share/icons/hicolor/256x256/apps/vnfap.png"
install -Dm 644 $HBB/res/scalable.svg "%{buildroot}/usr/share/icons/hicolor/scalable/apps/vnfap.svg"

%files
/usr/share/vnfap/*
/usr/share/vnfap/files/vnfap.service
/usr/share/icons/hicolor/256x256/apps/vnfap.png
/usr/share/icons/hicolor/scalable/apps/vnfap.svg
/usr/share/vnfap/files/vnfap.desktop
/usr/share/vnfap/files/vnfap-link.desktop

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
ln -sf /usr/share/vnfap/vnfap /usr/bin/vnfap
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
    rm /usr/bin/vnfap || true
    rmdir /usr/lib/vnfap || true
    rmdir /usr/local/vnfap || true
    rmdir /usr/share/vnfap || true
    rm /usr/share/applications/vnfap.desktop || true
    rm /usr/share/applications/vnfap-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
    rmdir /usr/lib/vnfap || true
    rmdir /usr/local/vnfap || true
  ;;
esac
