%global tl_name rescansync
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.0
Release:	%{tl_revision}.1
Summary:	Re-scan tokens with synctex information
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rescansync
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rescansync.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rescansync.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Allow users to execute saved code to typeset text while preserving
SyncTeX information.

