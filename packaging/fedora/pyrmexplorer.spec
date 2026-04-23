Name:           pyrmexplorer
Version:        1.3.2
Release:        1%{?dist}
Summary:        GUI explorer for reMarkable tablets

License:        GPL-3.0-or-later
URL:            https://github.com/bruot/pyrmexplorer
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  ImageMagick-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pip

Requires:       ImageMagick

%global __requires_exclude_from ^%{_libexecdir}/%{name}/.*$

%description
pyrmexplorer is a GUI explorer for reMarkable tablets.

%prep
%autosetup

%build
python3 -m pip install --user --upgrade pip
python3 -m pip install --user -r requirements.txt pyinstaller
./pyinstaller/compile-linux.sh

%install
install -d %{buildroot}%{_libexecdir}/%{name}
cp -a dist/rmexplorer/. %{buildroot}%{_libexecdir}/%{name}/

install -d %{buildroot}%{_bindir}
install -m 0755 packaging/linux/pyrmexplorer %{buildroot}%{_bindir}/pyrmexplorer

install -d %{buildroot}%{_datadir}/applications
install -m 0644 packaging/linux/pyrmexplorer.desktop \
    %{buildroot}%{_datadir}/applications/pyrmexplorer.desktop

install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m 0644 rmexplorer/icon.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/pyrmexplorer.svg

desktop-file-validate %{buildroot}%{_datadir}/applications/pyrmexplorer.desktop

%files
%license COPYING
%doc README
%{_bindir}/pyrmexplorer
%{_libexecdir}/%{name}/
%{_datadir}/applications/pyrmexplorer.desktop
%{_datadir}/icons/hicolor/scalable/apps/pyrmexplorer.svg

%changelog
* Thu Apr 23 2026 Codex <codex@openai.com> - 1.3.2-1
- Add Fedora RPM packaging and Linux PyInstaller build flow
