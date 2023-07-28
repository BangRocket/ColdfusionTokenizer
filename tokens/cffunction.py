import re
from cftoken import CFToken

class CFFunction(CFToken):
    
    FUNCTIONS = [
        'Abs', 'ACos', 'AddSOAPRequestHeader', 'AddSOAPResponseHeader', 'ArrayAppend',
        'ArrayAvg', 'ArrayClear', 'ArrayDeleteAt', 'ArrayInsertAt', 'ArrayIsDefined',
        'ArrayIsEmpty', 'ArrayLen', 'ArrayMax', 'ArrayMin', 'ArrayNew', 'ArrayPrepend',
        'ArrayResize', 'ArraySet', 'ArraySort', 'ArraySum', 'ArraySwap', 'ArrayToList',
        'Asc', 'ASin', 'ATan', 'Beat', 'BinaryDecode', 'BinaryEncode', 'BitAnd',
        'BitMaskClear', 'BitMaskRead', 'BitMaskSet', 'BitNot', 'BitOr', 'BitSHLN',
        'BitSHRN', 'BitXOr', 'Ceiling', 'CFusion_decrypt', 'CFusion_encrypt',
        'CharsetDecode', 'CharsetEncode', 'Chr', 'CJustify', 'Compare', 'CompareNoCase',
        'CompileRest', 'ComponentInfo', 'CompoundHash', 'ContractPath', 'Cos', 'CreateDecoder',
        'CreateObject', 'CreateUUId', 'CreateObject', 'CreateODBCDate', 'CreateODBCDateTime',
        'CreateODBCTime', 'CreateTime', 'CreateTimeSpan', 'CreateUniqueString', 'DateAdd',
        'DateCompare', 'DateConvert', 'DateDiff', 'DateFormat', 'DatePart', 'DateTimeFormat',
        'Day', 'DayOfWeek', 'DayOfWeekAsString', 'DayOfYear', 'DaysInMonth', 'DaysInYear',
        'DecrementValue', 'Decrypt', 'DecryptBinary', 'DeleteClientVariable', 'DESDecrypt',
        'DESEncrypt', 'DirectoryExists', 'DollarFormat', 'Duplicate', 'Each', 'Encrypt',
        'EncryptBinary', 'EntityDecode', 'EntityEncode', 'Exp', 'ExpandPath', 'Extract',
        'FileExists', 'Find', 'FindNoCase', 'FindOneOf', 'FirstDayOfMonth', 'Fix', 'FormatBaseN',
        'GetApplicationSettings', 'GetApplicationMetaData', 'GetAuthUser', 'GetBaseTagData',
        'GetBaseTagList', 'GetBaseTemplatePath', 'GetClientVariablesList',
        'GetComponentMetaData', 'GetContextRoot', 'GetCurrentTemplatePath',
        'GetDirectoryFromPath', 'GetEncoding', 'GetException', 'GetFileFromPath',
        'GetFileInfo', 'GetFunctionList', 'GetGatewayHelper', 'GetHttpTimeString',
        'GetK2ServerDocCount', 'GetK2ServerDocCountLimit', 'GetLocale',
        'GetLocaleDisplayName', 'GetMetaData', 'GetMetricData', 'GetPageContext',
        'GetProfileSections', 'GetProfileString', 'GetRequestData', 'GetScriptProtectNumLines',
        'GetSOAPRequest', 'GetSOAPRequestHeader', 'GetSOAPResponse',
        'GetSOAPResponseHeader', 'GetTempDirectory', 'GetTempFile', 'GetTickCount',
        'GetTimeZoneInfo', 'GetToken', 'GetTotalSpace', 'GetUserRoles', 'GetWriteableImageFormats',
        'Hash', 'Hash40', 'Hour', 'HTMLCodeFormat', 'HTMLEditFormat', 'IIf', 'ImageAddBorder',
        'ImageBlur', 'ImageClearRect', 'ImageCopy', 'ImageCreateCaptcha', 'ImageCrop',
        'ImageDilate', 'ImageDrawArc', 'ImageDrawBeveledRect', 'ImageDrawCubicCurve',
        'ImageDrawLine', 'ImageDrawLines', 'ImageDrawOval', 'ImageDrawPoint',
        'ImageDrawQuadraticCurve', 'ImageDrawRect', 'ImageDrawRoundRect', 'ImageDrawText',
        'ImageFlip', 'ImageGetBlob', 'ImageGetBufferedImage', 'ImageGetEXIFTag', 'ImageGetHeight',
        'ImageGetIPTCTag', 'ImageGetWidth', 'ImageGrayScale', 'ImageInfo', 'ImageNegative',
        'ImageNew', 'ImageOverlay', 'ImagePaste', 'ImageRead', 'ImageReadBase64',
        'ImageResize', 'ImageRotate', 'ImageRotateDrawingAxis', 'ImageScaleToFit',
        'ImageSetBackgroundColor', 'ImageSetDrawingColor', 'ImageSetDrawingStroke',
        'ImageSetDrawingTransparency', 'ImageSharpen', 'ImageShear', 'ImageShearDrawingAxis',
        'ImageTranslate', 'ImageTranslateDrawingAxis', 'ImageWrite', 'ImageWriteBase64',
        'IncrementValue', 'InputBaseN', 'Insert', 'Int', 'InvalidateOAuthaccesstoken', 'IsArray',
        'IsBinary', 'IsBoolean', 'IsCustomFunction', 'IsDate', 'IsDDX', 'IsDebugMode',
        'IsImage', 'IsImageFile', 'IsInstanceOf', 'IsJSON', 'IsLeapYear', 'IsNumeric',
        'IsNumericDate', 'IsObject', 'IsPDFFile', 'IsPDFObject', 'IsQuery',
        'IsSimpleValue', 'IsSOAPRequest', 'IsStruct', 'IsUserInAnyRole', 'IsUserInRole',
        'IsUserLoggedIn', 'IsValid', 'IsValidOauthaccesstoken', 'IsWDDX', 'IsXML', 'IsXMLAttribute',
        'IsXMLElement', 'IsXMLNode', 'IsXMLRoot', 'IsXSSFFile', 'IsXSSFPicture', 'IsXSSFShape',
        'IsXSSFSheet', 'IsXSSFWorkbook', 'JSStringFormat', 'LCase', 'Left', 'Len', 'ListAppend',
        'ListChangeDelims', 'ListContains', 'ListContainsNoCase', 'ListDeleteAt', 'ListFilter',
        'ListFind', 'ListFindNoCase', 'ListFirst', 'ListGetAt', 'ListInsertAt', 'ListLast',
        'ListLen', 'ListPrepend', 'ListQualify', 'ListReduce', 'ListRemoveDuplicates',
        'ListRest', 'ListSetAt', 'ListSort', 'ListToArray', 'ListValueCount', 'ListValueCountNoCase',
        'LJustify', 'LSParseCurrency', 'LSParseDateTime', 'LSParseEuroCurrency', 'LSParseNumber',
        'Max', 'Metaphone', 'Mid', 'Min', 'Minute', 'Month', 'MonthAsString', 'Now', 'NumberFormat',
        'ObjectEquals', 'ObjectLoad', 'ObjectSave', 'OnApplicationEnd', 'OnApplicationStart',
        'OnError', 'OnMissingMethod', 'OnMissingTemplate', 'OnRequest', 'OnRequestEnd',
        'OnRequestStart', 'OnSessionEnd', 'OnSessionStart', 'ParagraphFormat', 'ParseDateTime',
        'ParseNumber', 'Pi', 'PreserveSingleQuotes', 'Quarter', 'QueryAddColumn', 'QueryAddRow',
        'QueryColumnArray', 'QueryColumnCount', 'QueryColumnExists', 'QueryColumnList',
        'QueryConvertForGrid', 'QueryCurrentRow', 'QueryDeleteColumn', 'QueryDeleteRow',
        'QueryGetCell', 'QueryGetRow', 'QueryMap', 'QueryNew', 'QueryRecordCount', 'QueryReduce',
        'QueryRowData', 'QuerySetCell', 'Rand', 'Randomize', 'RandRange', 'REFind', 'REFindNoCase',
        'ReleaseComObject', 'RemoveChars', 'RemoveNumeric', 'RepeatString', 'Replace', 'ReplaceList',
        'ReplaceNoCase', 'REReplace', 'REReplaceNoCase', 'RESplit', 'RESplitNoCase', 'Reverse', 'RTrim',
        'Second', 'SendGatewayMessage', 'Serialize', 'SerializeJSON', 'SerializeXML', 'SessionId',
        'SessionInvalidate', 'SessionRotate', 'SessionTimeout', 'SetEncoding', 'SetLocale',
        'SetProfileString', 'SetVariable', 'Sgn', 'Sin', 'SpanExcluding', 'SpanIncluding', 'SpreadsheetAddAutoFilter',
        'SpreadsheetAddColumn', 'SpreadsheetAddFreezePane', 'SpreadsheetAddImage',
        'SpreadsheetAddInfo', 'SpreadsheetAddRow', 'SpreadsheetAddRows', 'SpreadsheetAddSplitPane',
        'SpreadsheetCreateSheet', 'SpreadsheetDeleteColumn', 'SpreadsheetDeleteColumns',
        'SpreadsheetDeleteRow', 'SpreadsheetDeleteRows', 'SpreadsheetFormatCell',
        'SpreadsheetFormatCellRange', 'SpreadsheetFormatColumn', 'SpreadsheetFormatColumns',
        'SpreadsheetFormatRow', 'SpreadsheetFormatRows', 'SpreadsheetGetCellComment',
        'SpreadsheetGetCellFormula', 'SpreadsheetGetCellValue', 'SpreadsheetInfo',
        'SpreadsheetMergeCells', 'SpreadsheetNew', 'SpreadsheetRead', 'SpreadsheetReadBinary',
        'SpreadsheetRemoveSheet', 'SpreadsheetSetActiveSheet', 'SpreadsheetSetActiveSheetNumber',
        'SpreadsheetSetCellComment', 'SpreadsheetSetCellFormula', 'SpreadsheetSetCellValue',
        'SpreadsheetSetColumnWidth', 'SpreadsheetSetFooter', 'SpreadsheetSetHeader',
        'SpreadsheetSetRowHeight', 'SpreadsheetShiftColumns', 'SpreadsheetShiftRows',
        'SpreadsheetWrite', 'Sqrt', 'StripCR', 'StructAppend', 'StructClear', 'StructCopy',
        'StructCount', 'StructDelete', 'StructEach', 'StructFilter', 'StructFind',
        'StructFindKey', 'StructFindValue', 'StructGet', 'StructInsert', 'StructIsEmpty',
        'StructKeyArray', 'StructKeyExists', 'StructKeyList', 'StructNew', 'StructSort',
        'StructUpdate', 'Tan', 'Throw', 'TimeFormat', 'ToBase64', 'ToBinary', 'ToScript', 'ToString',
        'Trace', 'TransactionCommit', 'TransactionRollback', 'Trim', 'UCase', 'URLDecode', 'URLEncodedFormat',
        'URLSessionFormat', 'Val', 'ValueArray', 'ValueList', 'VerifyClient', 'Week', 'Wrap', 'WriteBody',
        'WriteDump', 'WriteLog', 'WriteOutput', 'WSGetAllChannels', 'WSGetSubscribers', 'WSPublish',
        'WSSendMessage', 'WSSubscribe', 'WSSendMessage', 'XMLChildPos', 'XMLElemNew', 'XMLFormat',
        'XMLGetNodeType', 'XMLNew', 'XMLParse', 'XMLSearch', 'XMLTransform', 'XMLValidate',
        'Year', 'YesNoFormat'
    ]

    def __init__(self, value, line, col):
        super().__init__(value, line, col)
        self.function = value if value in self.FUNCTIONS else None

    def __str__(self):
        return f'CFFunctionToken({self.function})' if self.function else 'CFFunctionToken(UNKNOWN)'
    
    def tokenize_functions(self, text, line):
        for func in CFFunction.FUNCTIONS:
            if func in text:
                token = CFFunction(func, line, text.find(func))
                self.tokens.append(token)

