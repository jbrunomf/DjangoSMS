from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["brand_name"]

    def __str__(self):
        return self.brand_name

    def get_description_summary(self, length=50):
        """
        Returns a short summary of the description field,
        truncated to the specified length (default: 50 characters).
        """
        return (self.description[:length] + "...") if self.description and len(
            self.description) > length else self.description
