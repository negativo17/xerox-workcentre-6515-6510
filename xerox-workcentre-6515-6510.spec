Name:           xerox-workcentre-6515-6510
Version:        5.662.0.0
Release:        1%{?dist}
Summary:        Xerox WorkCentre 6515 / Phaser 6510 printer driver
License:        Xerox
URL:            https://www.support.xerox.com/en-us/product/workcentre-6515/content/144488
Source0:        https://download.support.xerox.com/pub/drivers/6510/drivers/win10/ar/Phaser_6510_%{version}_PPD_English.exe
BuildArch:      noarch

BuildRequires:  unrar

Requires:       cups

%description
Generic PPD driver for Xerox WorkCentre 6515 / Phaser 6510.

%prep
%setup -c -T
unrar -l %{SOURCE0} | sed -e '1,/.*{/d' -e '/}/{s/\(.*\)//;q}' > LICENSE
unrar x -c- %{SOURCE0}

%install
install -p -D -m644 xrx6515.ppd %{buildroot}%{_datadir}/ppd/xerox/xrx6515.ppd
install -p -D -m644 xrx6510.ppd %{buildroot}%{_datadir}/ppd/xerox/xrx6510.ppd

%files
%license LICENSE
%{_datadir}/ppd/xerox/xrx6515.ppd
%{_datadir}/ppd/xerox/xrx6510.ppd

%changelog
* Thu Jan 11 2024 Simone Caronni <negativo17@gmail.com> - 5.662.0.0-1
- First build.
