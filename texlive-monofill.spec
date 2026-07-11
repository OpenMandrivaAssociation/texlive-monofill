%global tl_name monofill
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Alignment of plain text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/monofill
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/monofill.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/monofill.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/monofill.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides horizontal alignment, as in the LaTeX command
\listfiles (or the author's longnamefilelist package). Uses may include
in-text tables, or even code listings.

