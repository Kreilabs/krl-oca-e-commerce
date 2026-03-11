odoo.define("website_sale_product_attachment.tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    tour.register(
        "website_sale_product_attachment_tour",
        {
            url: "/shop",
            test: true,
        },
        [
            {
                trigger: "#product_attachments_header button",
            },
        ]
    );
    return {};
});
