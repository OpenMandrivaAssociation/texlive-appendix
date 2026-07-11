%global tl_name appendix
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2c
Release:	%{tl_revision}.1
Summary:	Extra control of appendices
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/appendix
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/appendix.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/appendix.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/appendix.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The appendix package provides various ways of formatting the titles of
appendices. Also (sub)appendices environments are provided that can be
used, for example, for per chapter/section appendices. The word
'Appendix' or similar can be prepended to the appendix number for
article class documents. The word 'Appendices' or similar can be added
to the table of contents before the appendices are listed. The word
'Appendices' or similar can be typeset as a \part-like heading (page) in
the body. An appendices environment is provided which can be used
instead of the \appendix command.

