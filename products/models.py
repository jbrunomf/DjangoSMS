from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey("brands.Brand", on_delete=models.PROTECT, related_name="products")
    category = models.ForeignKey("categories.Category", on_delete=models.PROTECT, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.IntegerField(default=0)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
