%global debug_package %{nil}


Name:           cava
Version:        0.10.3
Release:        1
Summary:        C.A.V.A. is a bar spectrum analyzer for audio using ALSA for input
Group:          Terminal/Audio
License:        MIT
URL:            https://github.com/karlstav/cava
Source0:        %{url}/archive/%version.tar.gz


BuildRequires:  iniparser-devel
BuildRequires:  fftw-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  portaudio-devel
BuildRequires:  pkgconfig(wireplumber-0.5)
BuildRequires:  pkgconfig(sndio)
BuildRequires:  pkgconfig(jack)

Provides: cava

%description
%summary

%prep
%autosetup -p1
./autogen.sh


%build
%configure FONT_DIR=/lib/kbd/consolefonts LIBS=-lrt
make %{?_smp_mflags} \
    cava_LDFLAGS=


%install
%make_install
rm -f %{buildroot}%{_libdir}/libiniparser.{a,la,so}

%files
%license LICENSE
%doc README.md
%doc example_files
%{_bindir}/cava
/lib/kbd/consolefonts/cava.psf



