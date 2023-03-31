Name:		texlive-monofill
Version:	28140
Release:	2
Summary:	Alignment of plain text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/monofill
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/monofill.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/monofill.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/monofill.source.r%{version}.tar.xz
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
%doc %{_texmfdistdir}/doc/latex/monofill/Announce.txt
%doc %{_texmfdistdir}/doc/latex/monofill/README
%doc %{_texmfdistdir}/doc/latex/monofill/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/latex/monofill/monofill.pdf
#- source
%doc %{_texmfdistdir}/source/latex/monofill/monofill.tex
%doc %{_texmfdistdir}/source/latex/monofill/srcfiles.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
