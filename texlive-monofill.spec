# revision 27891
# category Package
# catalog-ctan /macros/latex/contrib/monofill
# catalog-date 2012-09-30 14:52:41 +0200
# catalog-license lppl1.3
# catalog-version 0.1b
Name:		texlive-monofill
Version:	0.1b
Release:	1
Summary:	Alignment of plain text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/monofill
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/monofill.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/monofill.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/monofill.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides horizontal alignment, as in the LaTeX
command \listfiles (or the author's longnamefilelist package).
Uses may include in-text tables, or even code listings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/monofill/monofill.RLS
%{_texmfdistdir}/tex/latex/monofill/monofill.sty
%doc %{_texmfdistdir}/doc/latex/monofill/README
%doc %{_texmfdistdir}/doc/latex/monofill/monofill.pdf
#- source
%doc %{_texmfdistdir}/source/latex/monofill/monofill.tex
%doc %{_texmfdistdir}/source/latex/monofill/srcfiles.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
