Name:		texlive-rescansync
Version:	63856
Release:	2
Summary:	Re-scan tokens with synctex information
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rescansync
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rescansync.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rescansync.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Allow users to execute saved code to typeset text while
preserving SyncTeX information.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/rescansync
%doc %{_texmfdistdir}/doc/latex/rescansync

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
