# -*-: coding utf-8 -*-
""" OrangeTV Snips skill. """


import requests
import json
import time
import os
import errno
import sys
import orange_setup

from color_utils import colors

class OrangeTV:
    """ OrangeTV Snips skill. """

    colormap= colors

    def __init__(self, hostname=None, username=None, locale=None):
        """Initialisation
        :param hostname: hostname for some OrangeTV
        :param username: OrangeTV username
        :param light_ids: Philips Hue light IDs
        """
        if hostname is None or username is None:
            setup= orange_setup.OrangeSetup()
            url= setup.bridge_url


            print str(url)
        else:
            url='http://{}/api/{}'.format(hostname, username)

        self.orangetv_endpoint = url + "/orangetv"
        self.groups_endpoint= url + "/groups"
        self.config_enpoint= url + "/config"

        self.orangetv_from_room = self._get_rooms_orangetv() 


    def requestChannelOrangeTV(self, color=None, location=None)
    	"""Turn on Channel OrangeTV in [location] with [color] color."""
    	orangetv_ids=self._get_orangetv_ids_from_room(location)

    	state = {"on": True}
    	if color != None:
    		state.update(self._get_orangetv_saturation(color))

    	self._post_state_to_ids(state, orangetv_ids)

    def _get_orangetv_saturation(self, color_name):
    	return self.colormap.get(color_name, {'orange': 0, 'sat': 0})
    	   


    def orangetv_on(self,location=None):
        self._post_state_to_ids({"on":True},self._get_orangetv_ids_from_room(location))
        print("Turn on")
    def orangetv_off(self,location):
        self._post_state_to_ids({"on":False},self._get_orangetv_ids_from_room(location))
        print("Turn off")        

    def _post_state_to_ids(self, params, orangetv_ids):
        """Post a state update to specyfied OrangeTV."""
        try:
            for orangetv_id in orangetv_ids:
                self._post_state(params, orangetv_id)
                time.sleep(0.2)
        except Exception as e:
            return
    def _post_state(self, params, orangetv_id):
        """Post a state update to a given orangetv.

        :param params: OrangeTV request parameters.
        :param orangetv_id: OrangeTV ID.
        """

        if (orangetv_id is None) or (params is None):
            return
        print("[Orange] Setting State for OrangeTV "+ str(orangetv_id)+ ": "+str(params))

        try:
            url= "{}/{}/state".format(self.orangetv_endpoint, orangetv_id)
            request.put(url, data=json.dumps(params), headers=None)
        except Exception as e:
            print("[Orange] Request timeout.")
            pass

    def _get_all_orangetv(self):
        """Return all orangetv"""
       orangetv=request.get(self.orangetv_endpoint).json()
       return orangetv.keys()

    def _get_orangetv_ids_from_room(self,room):
        """Returns the lsit of the orangetv in a [room] or all orangetv_ids if [room] is None"""

        if room is not None:
            room=room.lower()
        if room is None or self.orangetv_from_room.get(room) is None:
            retrun self._get_all_orangetv()
        
        return self.orangetv_from_room[room]

    def _get_rooms_orangetv(self):
        """Return a dic of OrangeTV"""
        groups =request.get(self.groups_endpoint).json()
        ids_from_room={}


        for key, value in groups.iteritems():
            group =value
            if group.get("class") is not None:
                ids_from_room[str.lower(str(group["class"]))] = [str(x) for x in group["orange"]]
        print"[OrangeTV] Available rooms: \n" + ("\n".join(ids_from_room.keys()))
        return ids_from_room


    if _name_=="_main_":
        ot=OrangeTV()

        ot.orangetv_on("Bedroom")
        print ot._get_all_orangetv()
