Name:		texlive-appendix
Version:	53718
Release:	1
Summary:	Extra control of appendices
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/appendix
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/appendix.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/appendix.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/appendix.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The appendix package provides various ways of formatting the
titles of appendices. Also (sub)appendices environments are
provided that can be used, for example, for per chapter/section
appendices. The word `Appendix' or similar can be prepended to
the appendix number for article class documents. The word
`Appendices' or similar can be added to the table of contents
before the appendices are listed. The word `Appendices' or
similar can be typeset as a \part-like heading (page) in the
body. An appendices environment is provided which can be used
instead of the \appendix command.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/appendix/appendix.sty
%doc %{_texmfdistdir}/doc/latex/appendix/README
%doc %{_texmfdistdir}/doc/latex/appendix/appendix.pdf
#- source
%doc %{_texmfdistdir}/source/latex/appendix/appendix.dtx
%doc %{_texmfdistdir}/source/latex/appendix/appendix.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
