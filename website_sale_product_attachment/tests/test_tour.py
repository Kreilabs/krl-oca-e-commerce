# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl)
# Copyright 2021 Tecnativa - Víctor Martínez

from base64 import b64encode

from odoo.tests import common


class TestWebsiteSaleProductAttachmentTourl(common.HttpCase):
    def setUp(self):
        super().setUp()
        self.product = self.env["product.template"].create(
            {
                "name": "Website Attachment Test Product",
                "list_price": 10.0,
                "website_published": True,
            }
        )
        attachment = self.env["ir.attachment"].create(
            {
                "name": "website_attachment_test.txt",
                "type": "binary",
                "datas": b64encode(b"website attachment test"),
                "mimetype": "text/plain",
                "public": True,
            }
        )
        self.product.website_attachment_ids = [(6, 0, attachment.ids)]

    def test_tour(self):
        self.start_tour(
            self.product.website_url,
            "website_sale_product_attachment_tour",
            login="admin",
        )
