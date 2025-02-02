from django.db import models


class StockMovementIn(models.Model):
    supplier = models.ForeignKey("suppliers.Supplier", on_delete=models.PROTECT, related_name="supplier_movements_in")
    product = models.ForeignKey("products.Product", on_delete=models.PROTECT, related_name="product_movements_in")
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'{self.product}'


class StockMovementOut(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.PROTECT, related_name="product_movements_out")
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'{self.product}'
