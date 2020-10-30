class LockerSerializer(serializers.Serializer):
    a = serializers.CharField(required=True, allow_blank=False, max_length=100)
    b = serializers.CharField(required=True, allow_blank=False, max_length=100)