#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : etr
Version  : 0.7.5
Release  : 1
URL      : https://downloads.sourceforge.net/project/extremetuxracer/releases/0.7.5/etr-0.7.5.tar.xz
Source0  : https://downloads.sourceforge.net/project/extremetuxracer/releases/0.7.5/etr-0.7.5.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: etr-bin = %{version}-%{release}
Requires: etr-data = %{version}-%{release}
Requires: etr-license = %{version}-%{release}
BuildRequires : pkgconfig(glu)
BuildRequires : pkgconfig(sfml-audio)
BuildRequires : pkgconfig(sfml-graphics)
BuildRequires : pkgconfig(sfml-system)
BuildRequires : pkgconfig(sfml-window)

%description
See http://sourceforge.net/projects/extremetuxracer/

%package bin
Summary: bin components for the etr package.
Group: Binaries
Requires: etr-data = %{version}-%{release}
Requires: etr-license = %{version}-%{release}

%description bin
bin components for the etr package.


%package data
Summary: data components for the etr package.
Group: Data

%description data
data components for the etr package.


%package doc
Summary: doc components for the etr package.
Group: Documentation

%description doc
doc components for the etr package.


%package license
Summary: license components for the etr package.
Group: Default

%description license
license components for the etr package.


%prep
%setup -q -n etr-0.7.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556302692
export LDFLAGS="${LDFLAGS} -fno-lto"
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1556302692
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/etr
cp COPYING %{buildroot}/usr/share/package-licenses/etr/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/etr

%files data
%defattr(-,root,root,-)
/usr/share/appdata/etr.appdata.xml
/usr/share/applications/etr.desktop
/usr/share/etr/char/beastie/finish.lst
/usr/share/etr/char/beastie/lostrace.lst
/usr/share/etr/char/beastie/preview.png
/usr/share/etr/char/beastie/shape.lst
/usr/share/etr/char/beastie/start.lst
/usr/share/etr/char/beastie/wonrace.lst
/usr/share/etr/char/boris/finish.lst
/usr/share/etr/char/boris/lostrace.lst
/usr/share/etr/char/boris/preview.png
/usr/share/etr/char/boris/shape.lst
/usr/share/etr/char/boris/start.lst
/usr/share/etr/char/boris/wonrace.lst
/usr/share/etr/char/characters.lst
/usr/share/etr/char/samuel/finish.lst
/usr/share/etr/char/samuel/lostrace.lst
/usr/share/etr/char/samuel/preview.png
/usr/share/etr/char/samuel/shape.lst
/usr/share/etr/char/samuel/start.lst
/usr/share/etr/char/samuel/wonrace.lst
/usr/share/etr/char/trixi/finish.lst
/usr/share/etr/char/trixi/lostrace.lst
/usr/share/etr/char/trixi/preview.png
/usr/share/etr/char/trixi/shape.lst
/usr/share/etr/char/trixi/start.lst
/usr/share/etr/char/trixi/wonrace.lst
/usr/share/etr/char/tux/finish.lst
/usr/share/etr/char/tux/lostrace.lst
/usr/share/etr/char/tux/preview.png
/usr/share/etr/char/tux/shape.lst
/usr/share/etr/char/tux/start.lst
/usr/share/etr/char/tux/wonrace.lst
/usr/share/etr/courses/default/bumpy_ride/course.dim
/usr/share/etr/courses/default/bumpy_ride/elev.png
/usr/share/etr/courses/default/bumpy_ride/items.lst
/usr/share/etr/courses/default/bumpy_ride/preview.png
/usr/share/etr/courses/default/bumpy_ride/terrain.png
/usr/share/etr/courses/default/bumpy_ride/trees.png
/usr/share/etr/courses/default/bunny_hill/course.dim
/usr/share/etr/courses/default/bunny_hill/elev.png
/usr/share/etr/courses/default/bunny_hill/items.lst
/usr/share/etr/courses/default/bunny_hill/preview.png
/usr/share/etr/courses/default/bunny_hill/terrain.png
/usr/share/etr/courses/default/bunny_hill/trees.png
/usr/share/etr/courses/default/challenge_one/course.dim
/usr/share/etr/courses/default/challenge_one/elev.png
/usr/share/etr/courses/default/challenge_one/items.lst
/usr/share/etr/courses/default/challenge_one/preview.png
/usr/share/etr/courses/default/challenge_one/terrain.png
/usr/share/etr/courses/default/challenge_one/trees.png
/usr/share/etr/courses/default/chinese_wall/course.dim
/usr/share/etr/courses/default/chinese_wall/elev.png
/usr/share/etr/courses/default/chinese_wall/items.lst
/usr/share/etr/courses/default/chinese_wall/preview.png
/usr/share/etr/courses/default/chinese_wall/terrain.png
/usr/share/etr/courses/default/chinese_wall/trees.png
/usr/share/etr/courses/default/chragis_gagiwaetter/course.dim
/usr/share/etr/courses/default/chragis_gagiwaetter/elev.png
/usr/share/etr/courses/default/chragis_gagiwaetter/preview.png
/usr/share/etr/courses/default/chragis_gagiwaetter/terrain.png
/usr/share/etr/courses/default/chragis_gagiwaetter/trees.png
/usr/share/etr/courses/default/courses.lst
/usr/share/etr/courses/default/downhill_fear/course.dim
/usr/share/etr/courses/default/downhill_fear/elev.png
/usr/share/etr/courses/default/downhill_fear/items.lst
/usr/share/etr/courses/default/downhill_fear/preview.png
/usr/share/etr/courses/default/downhill_fear/terrain.png
/usr/share/etr/courses/default/downhill_fear/trees.png
/usr/share/etr/courses/default/explore_mountains/course.dim
/usr/share/etr/courses/default/explore_mountains/elev.png
/usr/share/etr/courses/default/explore_mountains/items.lst
/usr/share/etr/courses/default/explore_mountains/preview.png
/usr/share/etr/courses/default/explore_mountains/terrain.png
/usr/share/etr/courses/default/explore_mountains/trees.png
/usr/share/etr/courses/default/frozen_lakes/course.dim
/usr/share/etr/courses/default/frozen_lakes/elev.png
/usr/share/etr/courses/default/frozen_lakes/items.lst
/usr/share/etr/courses/default/frozen_lakes/preview.png
/usr/share/etr/courses/default/frozen_lakes/terrain.png
/usr/share/etr/courses/default/frozen_lakes/trees.png
/usr/share/etr/courses/default/frozen_river/course.dim
/usr/share/etr/courses/default/frozen_river/elev.png
/usr/share/etr/courses/default/frozen_river/items.lst
/usr/share/etr/courses/default/frozen_river/preview.png
/usr/share/etr/courses/default/frozen_river/terrain.png
/usr/share/etr/courses/default/frozen_river/trees.png
/usr/share/etr/courses/default/hippo_run/course.dim
/usr/share/etr/courses/default/hippo_run/elev.png
/usr/share/etr/courses/default/hippo_run/items.lst
/usr/share/etr/courses/default/hippo_run/preview.png
/usr/share/etr/courses/default/hippo_run/terrain.png
/usr/share/etr/courses/default/hippo_run/trees.png
/usr/share/etr/courses/default/holygrail/course.dim
/usr/share/etr/courses/default/holygrail/elev.png
/usr/share/etr/courses/default/holygrail/items.lst
/usr/share/etr/courses/default/holygrail/preview.png
/usr/share/etr/courses/default/holygrail/terrain.png
/usr/share/etr/courses/default/holygrail/trees.png
/usr/share/etr/courses/default/in_search_of_vodka/course.dim
/usr/share/etr/courses/default/in_search_of_vodka/elev.png
/usr/share/etr/courses/default/in_search_of_vodka/items.lst
/usr/share/etr/courses/default/in_search_of_vodka/preview.png
/usr/share/etr/courses/default/in_search_of_vodka/terrain.png
/usr/share/etr/courses/default/in_search_of_vodka/trees.png
/usr/share/etr/courses/default/keep_country_tidy/course.dim
/usr/share/etr/courses/default/keep_country_tidy/elev.png
/usr/share/etr/courses/default/keep_country_tidy/preview.png
/usr/share/etr/courses/default/keep_country_tidy/terrain.png
/usr/share/etr/courses/default/keep_country_tidy/trees.png
/usr/share/etr/courses/default/milos_castle/course.dim
/usr/share/etr/courses/default/milos_castle/elev.png
/usr/share/etr/courses/default/milos_castle/items.lst
/usr/share/etr/courses/default/milos_castle/preview.png
/usr/share/etr/courses/default/milos_castle/terrain.png
/usr/share/etr/courses/default/milos_castle/trees.png
/usr/share/etr/courses/default/path_of_daggers/course.dim
/usr/share/etr/courses/default/path_of_daggers/elev.png
/usr/share/etr/courses/default/path_of_daggers/items.lst
/usr/share/etr/courses/default/path_of_daggers/preview.png
/usr/share/etr/courses/default/path_of_daggers/terrain.png
/usr/share/etr/courses/default/path_of_daggers/trees.png
/usr/share/etr/courses/default/penguins_cant_fly/course.dim
/usr/share/etr/courses/default/penguins_cant_fly/elev.png
/usr/share/etr/courses/default/penguins_cant_fly/items.lst
/usr/share/etr/courses/default/penguins_cant_fly/preview.png
/usr/share/etr/courses/default/penguins_cant_fly/terrain.png
/usr/share/etr/courses/default/penguins_cant_fly/trees.png
/usr/share/etr/courses/default/quiet_river/course.dim
/usr/share/etr/courses/default/quiet_river/elev.png
/usr/share/etr/courses/default/quiet_river/items.lst
/usr/share/etr/courses/default/quiet_river/preview.png
/usr/share/etr/courses/default/quiet_river/terrain.png
/usr/share/etr/courses/default/quiet_river/trees.png
/usr/share/etr/courses/default/secret_valleys/course.dim
/usr/share/etr/courses/default/secret_valleys/elev.png
/usr/share/etr/courses/default/secret_valleys/items.lst
/usr/share/etr/courses/default/secret_valleys/preview.png
/usr/share/etr/courses/default/secret_valleys/terrain.png
/usr/share/etr/courses/default/secret_valleys/trees.png
/usr/share/etr/courses/default/this_means_something/course.dim
/usr/share/etr/courses/default/this_means_something/elev.png
/usr/share/etr/courses/default/this_means_something/items.lst
/usr/share/etr/courses/default/this_means_something/preview.png
/usr/share/etr/courses/default/this_means_something/terrain.png
/usr/share/etr/courses/default/this_means_something/trees.png
/usr/share/etr/courses/default/tux_at_home/course.dim
/usr/share/etr/courses/default/tux_at_home/elev.png
/usr/share/etr/courses/default/tux_at_home/items.lst
/usr/share/etr/courses/default/tux_at_home/preview.png
/usr/share/etr/courses/default/tux_at_home/terrain.png
/usr/share/etr/courses/default/tux_at_home/trees.png
/usr/share/etr/courses/default/twisty_slope/course.dim
/usr/share/etr/courses/default/twisty_slope/elev.png
/usr/share/etr/courses/default/twisty_slope/items.lst
/usr/share/etr/courses/default/twisty_slope/preview.png
/usr/share/etr/courses/default/twisty_slope/terrain.png
/usr/share/etr/courses/default/twisty_slope/trees.png
/usr/share/etr/courses/default/wild_mountains/course.dim
/usr/share/etr/courses/default/wild_mountains/elev.png
/usr/share/etr/courses/default/wild_mountains/items.lst
/usr/share/etr/courses/default/wild_mountains/preview.png
/usr/share/etr/courses/default/wild_mountains/terrain.png
/usr/share/etr/courses/default/wild_mountains/trees.png
/usr/share/etr/courses/events.lst
/usr/share/etr/courses/extras/bronze_set/course.dim
/usr/share/etr/courses/extras/bronze_set/elev.png
/usr/share/etr/courses/extras/bronze_set/preview.png
/usr/share/etr/courses/extras/bronze_set/terrain.png
/usr/share/etr/courses/extras/bronze_set/trees.png
/usr/share/etr/courses/extras/comepeces/course.dim
/usr/share/etr/courses/extras/comepeces/elev.png
/usr/share/etr/courses/extras/comepeces/preview.png
/usr/share/etr/courses/extras/comepeces/terrain.png
/usr/share/etr/courses/extras/comepeces/trees.png
/usr/share/etr/courses/extras/courses.lst
/usr/share/etr/courses/extras/desperation/course.dim
/usr/share/etr/courses/extras/desperation/elev.png
/usr/share/etr/courses/extras/desperation/preview.png
/usr/share/etr/courses/extras/desperation/terrain.png
/usr/share/etr/courses/extras/desperation/trees.png
/usr/share/etr/courses/extras/el_reto/course.dim
/usr/share/etr/courses/extras/el_reto/elev.png
/usr/share/etr/courses/extras/el_reto/preview.png
/usr/share/etr/courses/extras/el_reto/terrain.png
/usr/share/etr/courses/extras/el_reto/trees.png
/usr/share/etr/courses/extras/follow_white_rabbit/course.dim
/usr/share/etr/courses/extras/follow_white_rabbit/elev.png
/usr/share/etr/courses/extras/follow_white_rabbit/preview.png
/usr/share/etr/courses/extras/follow_white_rabbit/terrain.png
/usr/share/etr/courses/extras/follow_white_rabbit/trees.png
/usr/share/etr/courses/extras/herrings_half_pipe/course.dim
/usr/share/etr/courses/extras/herrings_half_pipe/elev.png
/usr/share/etr/courses/extras/herrings_half_pipe/preview.png
/usr/share/etr/courses/extras/herrings_half_pipe/terrain.png
/usr/share/etr/courses/extras/herrings_half_pipe/trees.png
/usr/share/etr/courses/extras/i_like_spike_2/course.dim
/usr/share/etr/courses/extras/i_like_spike_2/elev.png
/usr/share/etr/courses/extras/i_like_spike_2/preview.png
/usr/share/etr/courses/extras/i_like_spike_2/terrain.png
/usr/share/etr/courses/extras/i_like_spike_2/trees.png
/usr/share/etr/courses/extras/inception/course.dim
/usr/share/etr/courses/extras/inception/elev.png
/usr/share/etr/courses/extras/inception/preview.png
/usr/share/etr/courses/extras/inception/terrain.png
/usr/share/etr/courses/extras/inception/trees.png
/usr/share/etr/courses/extras/laberinto/course.dim
/usr/share/etr/courses/extras/laberinto/elev.png
/usr/share/etr/courses/extras/laberinto/preview.png
/usr/share/etr/courses/extras/laberinto/terrain.png
/usr/share/etr/courses/extras/laberinto/trees.png
/usr/share/etr/courses/extras/penguins_day/course.dim
/usr/share/etr/courses/extras/penguins_day/elev.png
/usr/share/etr/courses/extras/penguins_day/preview.png
/usr/share/etr/courses/extras/penguins_day/terrain.png
/usr/share/etr/courses/extras/penguins_day/trees.png
/usr/share/etr/courses/extras/pygoscelis_adeliae/course.dim
/usr/share/etr/courses/extras/pygoscelis_adeliae/elev.png
/usr/share/etr/courses/extras/pygoscelis_adeliae/preview.png
/usr/share/etr/courses/extras/pygoscelis_adeliae/terrain.png
/usr/share/etr/courses/extras/pygoscelis_adeliae/trees.png
/usr/share/etr/courses/extras/rock_n_roll/course.dim
/usr/share/etr/courses/extras/rock_n_roll/elev.png
/usr/share/etr/courses/extras/rock_n_roll/preview.png
/usr/share/etr/courses/extras/rock_n_roll/terrain.png
/usr/share/etr/courses/extras/rock_n_roll/trees.png
/usr/share/etr/courses/extras/slide_or_fly/course.dim
/usr/share/etr/courses/extras/slide_or_fly/elev.png
/usr/share/etr/courses/extras/slide_or_fly/preview.png
/usr/share/etr/courses/extras/slide_or_fly/terrain.png
/usr/share/etr/courses/extras/slide_or_fly/trees.png
/usr/share/etr/courses/extras/snow_run_1/course.dim
/usr/share/etr/courses/extras/snow_run_1/elev.png
/usr/share/etr/courses/extras/snow_run_1/preview.png
/usr/share/etr/courses/extras/snow_run_1/terrain.png
/usr/share/etr/courses/extras/snow_run_1/trees.png
/usr/share/etr/courses/extras/snow_run_2/course.dim
/usr/share/etr/courses/extras/snow_run_2/elev.png
/usr/share/etr/courses/extras/snow_run_2/preview.png
/usr/share/etr/courses/extras/snow_run_2/terrain.png
/usr/share/etr/courses/extras/snow_run_2/trees.png
/usr/share/etr/courses/extras/the_long_ride/course.dim
/usr/share/etr/courses/extras/the_long_ride/elev.png
/usr/share/etr/courses/extras/the_long_ride/preview.png
/usr/share/etr/courses/extras/the_long_ride/terrain.png
/usr/share/etr/courses/extras/the_long_ride/trees.png
/usr/share/etr/courses/extras/touch_the_moon/course.dim
/usr/share/etr/courses/extras/touch_the_moon/elev.png
/usr/share/etr/courses/extras/touch_the_moon/preview.png
/usr/share/etr/courses/extras/touch_the_moon/terrain.png
/usr/share/etr/courses/extras/touch_the_moon/trees.png
/usr/share/etr/courses/extras/touristic_ride/course.dim
/usr/share/etr/courses/extras/touristic_ride/elev.png
/usr/share/etr/courses/extras/touristic_ride/preview.png
/usr/share/etr/courses/extras/touristic_ride/terrain.png
/usr/share/etr/courses/extras/touristic_ride/trees.png
/usr/share/etr/courses/extras/tuxway/course.dim
/usr/share/etr/courses/extras/tuxway/elev.png
/usr/share/etr/courses/extras/tuxway/preview.png
/usr/share/etr/courses/extras/tuxway/terrain.png
/usr/share/etr/courses/extras/tuxway/trees.png
/usr/share/etr/courses/extras/twists/course.dim
/usr/share/etr/courses/extras/twists/elev.png
/usr/share/etr/courses/extras/twists/preview.png
/usr/share/etr/courses/extras/twists/terrain.png
/usr/share/etr/courses/extras/twists/trees.png
/usr/share/etr/courses/extras/wild_ride/course.dim
/usr/share/etr/courses/extras/wild_ride/elev.png
/usr/share/etr/courses/extras/wild_ride/preview.png
/usr/share/etr/courses/extras/wild_ride/terrain.png
/usr/share/etr/courses/extras/wild_ride/trees.png
/usr/share/etr/courses/extras/wild_west_chute_out/course.dim
/usr/share/etr/courses/extras/wild_west_chute_out/elev.png
/usr/share/etr/courses/extras/wild_west_chute_out/preview.png
/usr/share/etr/courses/extras/wild_west_chute_out/terrain.png
/usr/share/etr/courses/extras/wild_west_chute_out/trees.png
/usr/share/etr/courses/groups.lst
/usr/share/etr/credits.lst
/usr/share/etr/env/environment.lst
/usr/share/etr/env/etr/cloudy/front.png
/usr/share/etr/env/etr/cloudy/frontH.png
/usr/share/etr/env/etr/cloudy/left.png
/usr/share/etr/env/etr/cloudy/leftH.png
/usr/share/etr/env/etr/cloudy/light.lst
/usr/share/etr/env/etr/cloudy/right.png
/usr/share/etr/env/etr/cloudy/rightH.png
/usr/share/etr/env/etr/evening/front.png
/usr/share/etr/env/etr/evening/frontH.png
/usr/share/etr/env/etr/evening/left.png
/usr/share/etr/env/etr/evening/leftH.png
/usr/share/etr/env/etr/evening/light.lst
/usr/share/etr/env/etr/evening/right.png
/usr/share/etr/env/etr/evening/rightH.png
/usr/share/etr/env/etr/night/front.png
/usr/share/etr/env/etr/night/frontH.png
/usr/share/etr/env/etr/night/left.png
/usr/share/etr/env/etr/night/leftH.png
/usr/share/etr/env/etr/night/light.lst
/usr/share/etr/env/etr/night/right.png
/usr/share/etr/env/etr/night/rightH.png
/usr/share/etr/env/etr/sunny/front.png
/usr/share/etr/env/etr/sunny/frontH.png
/usr/share/etr/env/etr/sunny/left.png
/usr/share/etr/env/etr/sunny/leftH.png
/usr/share/etr/env/etr/sunny/light.lst
/usr/share/etr/env/etr/sunny/right.png
/usr/share/etr/env/etr/sunny/rightH.png
/usr/share/etr/env/tuxracer/cloudy/front.png
/usr/share/etr/env/tuxracer/cloudy/left.png
/usr/share/etr/env/tuxracer/cloudy/light.lst
/usr/share/etr/env/tuxracer/cloudy/right.png
/usr/share/etr/env/tuxracer/evening/front.png
/usr/share/etr/env/tuxracer/evening/left.png
/usr/share/etr/env/tuxracer/evening/light.lst
/usr/share/etr/env/tuxracer/evening/right.png
/usr/share/etr/env/tuxracer/night/front.png
/usr/share/etr/env/tuxracer/night/left.png
/usr/share/etr/env/tuxracer/night/light.lst
/usr/share/etr/env/tuxracer/night/right.png
/usr/share/etr/env/tuxracer/sunny/front.png
/usr/share/etr/env/tuxracer/sunny/left.png
/usr/share/etr/env/tuxracer/sunny/light.lst
/usr/share/etr/env/tuxracer/sunny/right.png
/usr/share/etr/fonts/fonts.lst
/usr/share/etr/fonts/pc_20.ttf
/usr/share/etr/fonts/std.ttf
/usr/share/etr/fonts/stdbold.ttf
/usr/share/etr/music/calmrace-ks.ogg
/usr/share/etr/music/credits1-cp.ogg
/usr/share/etr/music/freezingpoint.ogg
/usr/share/etr/music/lostrace-ks.ogg
/usr/share/etr/music/music.lst
/usr/share/etr/music/options1-jt.ogg
/usr/share/etr/music/race1-jt.ogg
/usr/share/etr/music/raceintro-ks.ogg
/usr/share/etr/music/racing_themes.lst
/usr/share/etr/music/readme
/usr/share/etr/music/spunkyrace-ks.ogg
/usr/share/etr/music/start1-jt.ogg
/usr/share/etr/music/wonrace1-jt.ogg
/usr/share/etr/objects/finish.png
/usr/share/etr/objects/flag.png
/usr/share/etr/objects/herring.png
/usr/share/etr/objects/object_types.lst
/usr/share/etr/objects/shrub.png
/usr/share/etr/objects/snowy_tree1.png
/usr/share/etr/objects/start.png
/usr/share/etr/objects/tree_barren2.png
/usr/share/etr/players/avatar01.png
/usr/share/etr/players/avatar02.png
/usr/share/etr/players/avatar03.png
/usr/share/etr/players/avatar04.png
/usr/share/etr/players/avatar05.png
/usr/share/etr/players/avatar06.png
/usr/share/etr/players/avatar07.png
/usr/share/etr/players/avatar08.png
/usr/share/etr/players/avatar09.png
/usr/share/etr/players/avatar10.png
/usr/share/etr/players/avatar11.png
/usr/share/etr/players/avatar12.png
/usr/share/etr/players/avatar13.png
/usr/share/etr/players/avatar14.png
/usr/share/etr/players/avatar15.png
/usr/share/etr/players/avatar16.png
/usr/share/etr/players/avatar17.png
/usr/share/etr/players/avatars.lst
/usr/share/etr/resources/gui/checkmark.png
/usr/share/etr/resources/gui/checkmarks.png
/usr/share/etr/resources/gui/cupicon.png
/usr/share/etr/resources/gui/energymask.png
/usr/share/etr/resources/gui/herringicon2.png
/usr/share/etr/resources/gui/splash.png
/usr/share/etr/resources/gui/stars.png
/usr/share/etr/sounds/grass_slide.wav
/usr/share/etr/sounds/ice_slide.wav
/usr/share/etr/sounds/leaves_slide.wav
/usr/share/etr/sounds/mud_slide.wav
/usr/share/etr/sounds/pickup1.wav
/usr/share/etr/sounds/pickup2.wav
/usr/share/etr/sounds/pickup3.wav
/usr/share/etr/sounds/rock_slide.wav
/usr/share/etr/sounds/snow_slide.wav
/usr/share/etr/sounds/sounds.lst
/usr/share/etr/sounds/tree_hit.wav
/usr/share/etr/terrains/dirt01.png
/usr/share/etr/terrains/floor01.png
/usr/share/etr/terrains/floor02.png
/usr/share/etr/terrains/grass01.png
/usr/share/etr/terrains/grass02.png
/usr/share/etr/terrains/grass03.png
/usr/share/etr/terrains/ice.png
/usr/share/etr/terrains/ice01.png
/usr/share/etr/terrains/ice02.png
/usr/share/etr/terrains/ice03.png
/usr/share/etr/terrains/icy_floor01.png
/usr/share/etr/terrains/icy_grass03.png
/usr/share/etr/terrains/icy_grass04.png
/usr/share/etr/terrains/icy_pave01.png
/usr/share/etr/terrains/icy_pave04.png
/usr/share/etr/terrains/icy_pave05.png
/usr/share/etr/terrains/icy_rock06.png
/usr/share/etr/terrains/mud01.png
/usr/share/etr/terrains/pave01.png
/usr/share/etr/terrains/pave02.png
/usr/share/etr/terrains/pebbles01.png
/usr/share/etr/terrains/pebbles04.png
/usr/share/etr/terrains/pebbles05.png
/usr/share/etr/terrains/rock.png
/usr/share/etr/terrains/rock01.png
/usr/share/etr/terrains/rock02.png
/usr/share/etr/terrains/rock03.png
/usr/share/etr/terrains/rock04.png
/usr/share/etr/terrains/rock05.png
/usr/share/etr/terrains/rock06.png
/usr/share/etr/terrains/rock07.png
/usr/share/etr/terrains/sand01.png
/usr/share/etr/terrains/snow.png
/usr/share/etr/terrains/snow01.png
/usr/share/etr/terrains/snow02.png
/usr/share/etr/terrains/snow03.png
/usr/share/etr/terrains/snowy_grass03.png
/usr/share/etr/terrains/snowy_ice.png
/usr/share/etr/terrains/snowy_ice02.png
/usr/share/etr/terrains/snowy_ice03.png
/usr/share/etr/terrains/snowy_rock02.png
/usr/share/etr/terrains/snowy_rock06.png
/usr/share/etr/terrains/terrains.lst
/usr/share/etr/textures/checkbox.png
/usr/share/etr/textures/checkmark_small.png
/usr/share/etr/textures/energymask2.png
/usr/share/etr/textures/gaugeenergymask.png
/usr/share/etr/textures/gaugeoutline.png
/usr/share/etr/textures/gaugespeedmask.png
/usr/share/etr/textures/herringicon.png
/usr/share/etr/textures/light_butt.png
/usr/share/etr/textures/listbox_arrows.png
/usr/share/etr/textures/mask_outline2.png
/usr/share/etr/textures/menu_bottom_left.png
/usr/share/etr/textures/menu_bottom_right.png
/usr/share/etr/textures/menu_title.png
/usr/share/etr/textures/menu_top_left.png
/usr/share/etr/textures/menu_top_right.png
/usr/share/etr/textures/mirror_butt.png
/usr/share/etr/textures/mouse_cursor.png
/usr/share/etr/textures/random_butt.png
/usr/share/etr/textures/snow1.png
/usr/share/etr/textures/snow2.png
/usr/share/etr/textures/snow3.png
/usr/share/etr/textures/snow_butt.png
/usr/share/etr/textures/snowparticles.png
/usr/share/etr/textures/snowstart.png
/usr/share/etr/textures/snowstop.png
/usr/share/etr/textures/snowtrack.png
/usr/share/etr/textures/speedknob2.png
/usr/share/etr/textures/speedmeter.png
/usr/share/etr/textures/splash_1.png
/usr/share/etr/textures/textures.lst
/usr/share/etr/textures/timeicon.png
/usr/share/etr/textures/tuxbonus.png
/usr/share/etr/textures/wind_butt.png
/usr/share/etr/textures/ziff032.png
/usr/share/etr/translations/cs_CZ.lst
/usr/share/etr/translations/de_DE.lst
/usr/share/etr/translations/es_ES.lst
/usr/share/etr/translations/fi_FI.lst
/usr/share/etr/translations/fr_FR.lst
/usr/share/etr/translations/languages.lst
/usr/share/etr/translations/pl_PL.lst
/usr/share/etr/translations/xx_XX.lst
/usr/share/pixmaps/etr.png
/usr/share/pixmaps/etr.svg

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/etr/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/etr/COPYING