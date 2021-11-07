"""
    Autobahn App API

    Was passiert auf Deutschlands Bundesstraßen? API für aktuelle Verwaltungsdaten zu Baustellen, Staus und Ladestationen. Außerdem Zugang zu Verkehrsüberwachungskameras und vielen weiteren Datensätzen.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland from deutschland import autobahn
from deutschland.autobahn.model.coordinate import Coordinate
from deutschland.autobahn.model.display_type import DisplayType
from deutschland.autobahn.model.extent import Extent
from deutschland.autobahn.model.lorry_parking_feature_icon import LorryParkingFeatureIcon
from deutschland.autobahn.model.multiline_text import MultilineText
from deutschland.autobahn.model.point import Point
from deutschland.autobahn.model.road_event_all_of import RoadEventAllOf
from deutschland.autobahn.model.road_item import RoadItem
globals()['Coordinate'] = Coordinate
globals()['DisplayType'] = DisplayType
globals()['Extent'] = Extent
globals()['LorryParkingFeatureIcon'] = LorryParkingFeatureIcon
globals()['MultilineText'] = MultilineText
globals()['Point'] = Point
globals()['RoadEventAllOf'] = RoadEventAllOf
globals()['RoadItem'] = RoadItem
from deutschland.autobahn.model.road_event import RoadEvent


class TestRoadEvent(unittest.TestCase):
    """RoadEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRoadEvent(self):
        """Test RoadEvent"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RoadEvent()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
