from rest_framework import serializers

from .models import Dataset, RelatedDocument
class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    keyword = serializers.RelatedField(many=True, source='tags')
    modified = serializers.DateField(source='last_update')
    publisher = serializers.RelatedField(source='publisher')
    identifier = serializers.CharField(source='unique_identifer')
    accessLevel = serializers.CharField(source='public_access_level')
    accessLevelComment = serializers.CharField(source='access_level_comment')
    bureauCode = serializers.RelatedField(source='bureau_code')
    programCode = serializers.RelatedField(source='program_code')
    accessURL = serializers.CharField(source='download_url')
    webService = serializers.CharField(source='endpoint')
    license = serializers.RelatedField(source='license')
    temporal = serializers.SerializerMethodField('temporal_calc')
    dataDictionary = serializers.CharField(source='data_dictionary')
    accuralPeriodicity = serializers.CharField(source='frequency')
    landingPage = serializers.CharField(source='landing_page')
    references = serializers.RelatedField(many=True)
    issued = serializers.DateField(source='release_date')
    
    def temporal_calc(self, obj):
        return "%s/%s" % (obj.temporal_start, obj.temporal_end)
    
    class Meta:
        model = Dataset
        fields = ('title', 'description', 'keyword', 'modified', 'publisher', 'identifier', 'accessLevel', 'accessLevelComment', 'bureauCode', 'programCode', 'accessURL', 'webService', 'license', 'temporal', 'dataDictionary', 'accuralPeriodicity', 'landingPage', 'references', 'issued')
        
        # spatial, category, data quality, languague, uii