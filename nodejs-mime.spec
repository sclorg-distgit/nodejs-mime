%{?scl:%scl_package nodejs-mime}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-mime
Version:        1.2.11
Release:        3%{?dist}
Summary:        A comprehensive library for mime-type mapping

Group:          System Environment/Libraries
License:        MIT
URL:            https://github.com/broofa/node-mime
Source0:        http://registry.npmjs.org/mime/-/mime-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

%description
Comprehensive MIME type mapping API. Includes all 600+ types and 800+ extensions
defined by the Apache project, plus additional types submitted by the node.js
community.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{nodejs_sitelib}/mime
cp -pr package.json types mime.js %{buildroot}%{nodejs_sitelib}/mime
%nodejs_symlink_deps

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/mime
%doc LICENSE README.md

%changelog
* Tue Mar 04 2014 Tomas Hrcka <thrcka@redhat.com> - 1.2.11-3
- Add missing nodejs_symlink_deps macro

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 1.2.11-2
- replace provides and requires with macro

* Mon Aug 26 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.11-1
- update to upstream release 1.2.11
- add ExclusiveArch logic

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.10-1
- new upstream release 1.2.10

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.9-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.9-2
- add macro for EPEL6 dependency generation

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.9-2
- Add support for software collections

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.9-1
- new upstream release 1.2.9

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.7-2
- add missing build section
- fix URL

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.7-1
- initial package generated by npm2rpm
