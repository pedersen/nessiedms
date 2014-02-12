This file is for you to describe the nessiewiki application. Typically
you would include information such as the information below:

Installation and Setup
======================

Install ``nessiewiki`` using the setup.py script::

    $ cd nessiewiki
    $ python setup.py develop

Create the project database for any model classes defined::

    $ gearbox setup-app

Start the paste http server::

    $ gearbox serve

While developing you may want the server to reload after changes in package files (or its dependencies) are saved. This can be achieved easily by adding the --reload option::

    $ gearbox serve --reload --debug

Then you are ready to go.

What Does This Do?
==================

Multiple Volumes
    A volume is top level item, and would normally be a wiki unto
    itself. Sometimes, some wikis will serve up sub-wikis. For
    instance, the Fallout WIki has sub-wikis for Fallout, Fallout 2,
    Fallout 3, Fallout New Vegas, etc. In Nessie Wiki, each of those
    sub-wikis would be their own volume.

Nestable Volumes
    Volumes can be nested. This is especially useful for sites like
    the Fallout wiki, which could create a complex layout using
    this. Fallout 1/2/3 could each be separate volumes, along with a
    separate "Creatures of Fallout" volume which could have its
    individual pages symlinked into the subvolume "Creatures" for each
    game. I'm not entirely sure what the implications are for the
    security model for this yet, either. Furthermore, entire volumes
    could be nested. For example, volumes could be made for each genus
    of animal in the world, and then phylum volumes could be made to
    group the genuses entirely. This could trickle up still further
    through the taxonomies.

Symlinked Pages
    Pages are not limited to appearing in one volume; they can appear
    in multiple volumes.

Non-Orphanable Pages
    Every page has a parent. If a parent page is deleted, then all
    child pages get linked to the parent of the deleted page. Each
    volume has a front page that acts as the ultimate parent page of
    that volume.

Security
    Each volume supports its own permissions. A person may be an admin
    in one volume, and a reader in another. The entire installation
    will also support the idea of a super admin, somebody who has the
    permission to do anything in the installation

Domain Volumes
    A given domain can also serve as a pointer for a volume in the
    installation. Furthermore, that volume can be hidden if it is not
    accessed via that domain name. Note that domain, in this case,
    refers to a DNS domain or subdomain.

Theme-ability
    Nessie Wiki supports using custom themes on a per volume basis. An
    option needs to exist to allow sub-volumes to override the parent
    volume's theme.

Customizable sub-volume names
    The default will be volume, part, chapter. However, a playwright
    could use act, scene. This customization should be on a per-volume
    basis, and not be able to be overridden by sub-volumes.

Automated Phrase Cross-Referencing
    Some way of automatically linking phrases to useful pages. I think
    that Lucene has some of this built in, but I don't know. Using the
    Fallout wiki idea, the phrase "deadly creature" might link to the
    Deathclaw page.

Per Page Plugins
    This would allow for different page types to be created and
    rendered, resulting in new uses. For instance, a ticket tracker
    plugin could be made that would allow for tickets to be entered
    and tracked, along with a custom display.

Templates
    Templates for a given page should be able to be defined by the
    site, by the volume, and by any associated plugins. This would
    allow for easy, consistent formatting for games, or for pictures,
    etc.

Scheduled Jobs
    A way to run background jobs on a scheduled basis. Volumes should
    also be regularly exported to PDF and epub. Doing it on demand,
    for any decently sized volume, will be impractical. A scheduled
    job that runs, waits an hour, and checks to see if it needs to be
    re-run, would be an ideal solution.

Versioned History
    The system needs to keep track of previous versions. It also needs
    to let an admin delete versions from history entirely. Should it
    use git/mercurial? Or just store whole versions of documents?

How URLs Should Look
====================

http://www.example.com/@volume1/mainpage
http://www.example.com/@volume1
http://www.example.com/
http://www.example.com/mainpage
http://example.com/@volume1
http://example.com/@volume1/mainpage

Note that a default volume will need to be specified, and a default
home page for that volume. That would mean that all the above URLs
should point to the same location, assuming that volume1 is the
default volume, and mainpage is the default page for that volume.

Domains can direct to specific volumes, as well.

http://volume1.example.com/ would point to volume1's default page.
http://www.volume1.com/ would also point to volume1's default page.

A problem exists with these two URLs, specifically when it comes to volumes.

http://www.example.com/mainpage
http://www.example.com/@volume2/mainpage

How to disambiguate when a volume is being explicitly named in a URL,
versus a page that happens to have the same name as a volume? The @
character is the answer. When a URL component has an @character at the
front of it, it always points to a volume by name.
