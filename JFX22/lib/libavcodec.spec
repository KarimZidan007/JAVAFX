Name:           libavcodec
Version:        54.92.100
Release:        1%{?dist}
Summary:        FFmpeg library for encoding/decoding audio and video

License:        LGPL-2.1+
URL:            https://www.ffmpeg.org/
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64

Requires:       libavformat = %{version}
Requires:       libavutil = %{version}
Requires:       libswscale = %{version}
Requires:       libavfilter = %{version}
Requires:       libpostproc = %{version}
Requires:       libavresample = %{version}

%description
FFmpeg is a complete, cross-platform solution to record, convert, and stream audio and video. This package contains the libraries for encoding and decoding audio and video streams.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/lib
cp -a libavcodec.so* %{buildroot}/usr/lib/

%files
/usr/lib/libavcodec.so.*

