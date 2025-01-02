from django.contrib import admin
from .models import SensorData
from .models import VideoPost

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    # 管理画面で表示するフィールド
    list_display = ('timestamp', 'temperature', 'humidity', 'illuminance')

    # 編集可能なフィールド
    fields = ('timestamp', 'temperature', 'humidity', 'illuminance')

    # 日付と時刻を変更可能にする
    readonly_fields = []  # 必要なら`readonly_fields`を空にしてtimestampを編集可能にする

    # 日時フィールドのフォーマットをカスタマイズ可能
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'timestamp':
            kwargs['widget'] = admin.widgets.AdminSplitDateTime()
        return super().formfield_for_dbfield(db_field, **kwargs)
    
    
@admin.register(VideoPost)
class VideoPostAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'result', 'video_url')
    search_fields = ('user__username', 'result', 'notes')
    list_filter = ('result', 'date')