#!/usr/bin/env python

import os, hashlib
import gconf, gtk.gdk, gnomevfs, gobject

def md5sum(value):
    md5 = hashlib.md5()
    md5.update(value)
    return md5.hexdigest()

class Background(object):

    def __init__(self):
        self.client = gconf.client_get_default()
        self.display = gtk.gdk.display_get_default()
        self.screen = self.display.get_default_screen()
        self.background_key = "/desktop/gnome/background/picture_filename"
        self.background_opts_key = "/desktop/gnome/background/picture_options"

    def get_screen_size(self):
        return (self.screen.get_width(), self.screen.get_height())

    def get_monitors(self):
        monitors = []
        for n in range(self.screen.get_n_monitors()):
            g = self.screen.get_monitor_geometry(n)
            monitors.append((g.width, g.height, g.x, g.y))
        return monitors

    def get_background(self):
        return self.client.get_string(self.background_key)

    def set_background(self, background, options=None):
        self.client.set_string(self.background_key, background)
        self.client.set_string(self.background_opts_key, options or 'scaled')



class Thumbnails(dict):

    def __init__(self):
        self.thumbnail_dir = os.path.expanduser('~/.thumbnails')
        if not os.path.isdir(self.thumbnail_dir):
            os.makedirs(self.thumbnail_dir)
        self.thumbnail_cache = {}
        self.thumbnail_sizes = {
                'normal': (128, 128),
                'large': (256, 256),
                }

    def get_key(self, location, size):
        key = md5sum(location)
        return os.path.join(self.thumbnail_dir, size, '%s.%s' % (key, 'png'))

    def get_path(self, uri):
        return gnomevfs.get_local_path_from_uri(uri)

    def get_uri(self, path):
        return gnomevfs.get_uri_from_local_path(path)

    def create(self, path, thumbnail, size):
        try:
            pb = gtk.gdk.pixbuf_new_from_file_at_size(path,
                    *self.thumbnail_sizes[size])
        except gobject.GError: # probably a corrupt image
            return None
        tdir = os.path.join(self.thumbnail_dir, size)
        if not os.path.isdir(tdir): os.makedirs(tdir)
        pb.save(thumbnail, 'png')
        return pb

    def get(self, uri, size):
        if not uri.startswith('file://'): uri = self.get_uri(uri)
        thumbnail = self.get_key(uri, size)
        if thumbnail in self.thumbnail_cache:
            pb = self.thumbnail_cache[thumbnail]
        else:
            if not os.path.isfile(thumbnail):
                pb = self.create(self.get_path(uri), thumbnail, size)
            else:
                pb = gtk.gdk.pixbuf_new_from_file_at_size(
                        thumbnail, *self.thumbnail_sizes[size])
            self.thumbnail_cache[thumbnail] = pb
        return pb

    def get_large(self, uri):
        return self.get(uri, 'large')

    def get_normal(self, uri):
        return self.get(uri, 'normal')
