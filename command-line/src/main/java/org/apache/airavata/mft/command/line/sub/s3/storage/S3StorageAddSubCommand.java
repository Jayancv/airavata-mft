/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.airavata.mft.command.line.sub.s3.storage;

import org.apache.airavata.mft.api.client.MFTApiClient;
import org.apache.airavata.mft.common.AuthToken;
import org.apache.airavata.mft.credential.stubs.s3.S3Secret;
import org.apache.airavata.mft.credential.stubs.s3.S3SecretCreateRequest;
import org.apache.airavata.mft.resource.service.s3.S3StorageServiceGrpc;
import org.apache.airavata.mft.resource.stubs.s3.storage.S3Storage;
import org.apache.airavata.mft.resource.stubs.s3.storage.S3StorageCreateRequest;
import org.apache.airavata.mft.resource.stubs.storage.common.SecretForStorage;
import org.apache.airavata.mft.resource.stubs.storage.common.StorageCommonServiceGrpc;
import org.apache.airavata.mft.resource.stubs.storage.common.StorageType;
import picocli.CommandLine;

import java.util.concurrent.Callable;

@CommandLine.Command(name = "add")
public class S3StorageAddSubCommand implements Callable<Integer> {

    @CommandLine.Option(names = {"-n", "--name"}, description = "Storage Name", required = true)
    private String remoteName;

    @CommandLine.Option(names = {"-b", "--bucket"}, description = "Bucket Name", required = true)
    private String bucket;

    @CommandLine.Option(names = {"-r", "--region"}, description = "Region", required = true)
    private String region;

    @CommandLine.Option(names = {"-e", "--endpoint"}, description = "S3 API Endpoint. For AWS S3 use https://s3.<REGION>.amazonaws.com", required = true)
    private String endpoint;

    @CommandLine.Option(names = {"-k", "--key"}, description = "Access Key", required = true)
    private String accessKey;

    @CommandLine.Option(names = {"-s", "--secret"}, description = "Access Secret", required = true)
    private String accessSecret;

    @CommandLine.Option(names = {"-t", "--token"}, description = "Session Token", defaultValue = "")
    private String sessionToken;

    @Override
    public Integer call() throws Exception {

        AuthToken authToken = AuthToken.newBuilder().build();

        MFTApiClient mftApiClient = MFTApiClient.MFTApiClientBuilder.newBuilder().build();

        S3Secret s3Secret = mftApiClient.getSecretServiceClient().s3()
                .createS3Secret(S3SecretCreateRequest.newBuilder()
                        .setAccessKey(accessKey)
                        .setSecretKey(accessSecret)
                        .setSessionToken(sessionToken)
                        .setAuthzToken(authToken).build());

        S3StorageServiceGrpc.S3StorageServiceBlockingStub s3StorageClient = mftApiClient.getStorageServiceClient().s3();
        StorageCommonServiceGrpc.StorageCommonServiceBlockingStub commonStorageClient = mftApiClient.getStorageServiceClient().common();

        S3Storage s3Storage = s3StorageClient.createS3Storage(S3StorageCreateRequest.newBuilder()
                .setName(remoteName)
                .setEndpoint(endpoint)
                .setBucketName(bucket)
                .setRegion(region).build());

        commonStorageClient.registerSecretForStorage(SecretForStorage.newBuilder()
                .setStorageId(s3Storage.getStorageId())
                .setSecretId(s3Secret.getSecretId())
                .setStorageType(StorageType.S3).build());

        System.out.println("Storage Id " + s3Storage.getStorageId());
        return 0;
    }
}
