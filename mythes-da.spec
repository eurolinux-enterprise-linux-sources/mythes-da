Name: mythes-da
Summary: Danish thesaurus
%define upstreamid 20100629.15.16
Version: 0.%{upstreamid}
Release: 6%{?dist}
Source: http://extensions.services.openoffice.org/e-files/1388/12/DanskeSynonymer.oxt
Group: Applications/Text
URL: http://synonym.oooforum.dk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2 or LGPLv2 or MPLv1.1
BuildArch: noarch
Requires: mythes

%description
Danish thesaurus.

%prep
%setup -q -c

%build
for i in README_th_da_DK.txt README_th_da_DK.txt README_th_en-US.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_da_DK.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_da_DK_v2.dat
cp -p th_da_DK.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_da_DK_v2.idx

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_da_DK.txt README_th_en-US.txt release_note.txt
%{_datadir}/mythes/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20100629.15.16-6
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100629.15.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100629.15.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100629.15.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100629.15.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 02 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100629.15.16
- latest version

* Sat Apr 03 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100126.13.05-2
- mythes now owns /usr/share/mythes

* Thu Jan 28 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100126.13.05-1
- latest version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090522-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090522-2
- tidy spec

* Sat May 23 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090522-1
- latest version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-0.2.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Caolán McNamara <caolanm@redhat.com> - 0.1.9-0.1.beta
- initial version
